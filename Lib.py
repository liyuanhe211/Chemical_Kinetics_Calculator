# -*- coding: utf-8 -*-
__author__ = 'LiYuanhe'

import sys
import os
import math
import copy
import shutil
import re
import time
import random
import subprocess
from collections import OrderedDict
from Python_Lib.My_Lib_Stock import *
from scipy.optimize import fsolve
import numpy as np


# All SI units
# conc: Concentration in mol/m^3
# P: Pressure in pa
# ΔG: Activation Gibbs free energy in J/mol
# T: Temperature in K
# t: Time
# σ: degeneracy，http://sobereva.com/310
# Δn: 0 for unimolecular, 1 for bimolecular
# k_TST: TST kinetic constant, first order s^-1, second order m^3·mol^-1·s^-1


def get_k_TST(Δn, σ, T, ΔG):
    """

    TST rate constant
    k_TST = (σ k_B T / h) * (R T/P0)^(n_TS - n_Sub) * exp( -ΔG≠ / R T)

    Returns:

    """
    return (σ * k_B * T / h) * ((R * T / atm__Pa) ** Δn) * math.exp(-ΔG / R / T)


get_k_TST_vectorize = np.vectorize(get_k_TST)


# print(get_k_TST(1,1,298,15000))


def solve_equation(func, initial_guess):
    root = fsolve(func, initial_guess)
    print("Original root:", root)
    ret = []
    for i in root:
        if np.isclose(func(i), 0.):
            if not any(np.isclose(x, i) for x in ret):
                ret.append(i)
    if len(ret) == 1:
        return ret[0]
    else:
        print("Solution not singular.")
        from Python_Lib.My_Lib_PyQt6 import warning_UI
        warning_UI("No valid solution find in the range set by the author.")
        return ret


def solve_for_ΔG(k_TST, Δn, σ, T):
    k_TST_unit = "m3·mol-1·s-1" if Δn else "s-1"

    def func(ΔG):
        return np.log(get_k_TST_vectorize(Δn, σ, T, ΔG) / k_TST)

    ret = solve_equation(func, 50000)

    print(f"Solve ΔG from TST.\n"
          f"   Δn: {Δn}, σ: {σ}, T: {T} K, rate constant: {k_TST} {k_TST_unit}. Answer: {ret} J/mol.")
    return ret


# print(solve_for_ΔG(0.89/1000,1,1,298))

def solve_for_T(k_TST, Δn, σ, ΔG):
    k_TST_unit = "m3·mol-1·s-1" if Δn else "s-1"

    def func(T):
        return np.log(get_k_TST_vectorize(Δn, σ, T, ΔG) / k_TST)

    ret = solve_equation(func, 300)
    print(f"Solve T from TST.\n"
          f"    Δn: {Δn}, σ: {σ}, ΔG: {ΔG} J/mol, rate constant: {k_TST} {k_TST_unit}. Answer: {ret} K.")
    return ret


def first_order_reaction_time(k_TST, conv):
    half_life_count = math.log((1 - conv), 1 / 2)
    half_life = math.log(2) / k_TST
    ret = half_life_count * half_life
    print(f"Calculate time from first order kinetics.\n"
          f"    Rate constant: {k_TST} s^-1, conversion: {conv}. Answer: {ret} s.")
    return ret


def first_order_conversion(k_TST, rxn_time):
    half_life = math.log(2) / k_TST
    half_life_count = rxn_time / half_life
    if half_life_count > 100:  # conversion too complete, return 100%
        ret = 1
    else:
        ret = 1 - 1 / 2 ** half_life_count
    print(f"Calculate conv from first order kinetics.\n"
          f"    Rate constant: {k_TST} s^-1, time: {rxn_time} s. Answer: {ret}.")
    return ret


def first_order_k_TST(conv, rxn_time):
    half_life_count = math.log((1 - conv), 1 / 2)
    half_life = rxn_time / half_life_count
    ret = math.log(2) / half_life
    print(f"Calculate k from first order kinetics.\n"
          f"    Conversion: {conv}, time: {rxn_time} s. Answer: {ret} s^-1.")
    return ret


def second_order_reaction_time_A_plus_A(k_TST, conv, conc):
    """
    1 / [A] = k_TST * t + 1 / [A]_0
    (1 / [A] - 1 / [A]_0) / k_TST
    """

    target_conc = conc * (1 - conv)
    ret = (1 / target_conc - 1 / conc) / k_TST
    print(f"Calculate time from A+A second order kinetics.\n"
          f"    Rate constant: {k_TST} m^3·mol^-1·s^-1, conversion: {conv} s, concentration: {conc} mol/m^3. Answer: {ret} s.")
    return ret


def second_order_conv_A_plus_A(k_TST, rxn_time, conc):
    """
    1 / [A] = k_TST * t + 1 / [A]_0
    """

    end_conc = 1 / (k_TST * rxn_time + 1 / conc)
    conv = 1 - end_conc / conc
    print(f"Calculate conv from second order kinetics.\n"
          f"    Rate constant: {k_TST} m^3·mol^-1·s^-1, time: {rxn_time} s, concentration: {conc} mol/m^3. Answer: {conv}.")
    return conv


def second_order_k_TST_A_plus_A(conv, rxn_time, conc):
    """
    1 / [A] = k_TST * t + 1 / [A]_0
    (1 / A - 1 / A0)/t = k_TST
    """

    A = conc * (1 - conv)
    A0 = conc
    ret = (1 / A - 1 / A0) / rxn_time
    print(f"Calculate k from A+A second order kinetics.\n"
          f"    Conversion: {conv}, time: {rxn_time} s, concentration: {conc} mol/m^3. Answer: {ret} m3·mol-1·s-1.")
    return ret


def second_order_reaction_time_A_plus_B(k_TST, conv, conc1, conc2):
    """
    ln([A]/[B]) = k_TST * ([A]_0 - [B]_0) * time + ln([A]_0/[B]_0)
    """
    A0, B0 = min(conc1, conc2), max(conc1, conc2)
    A, B = A0 - A0 * conv, B0 - A0 * conv
    ret = (math.log(A / B) - math.log(A0 / B0)) / k_TST / (A0 - B0)
    print(
        f"Calculate time from A+B second order kinetics.\n"
        f"    Rate constant: {k_TST} m^3·mol^-1·s^-1, conversion: {conv} s, concentrations: {conc1}, {conc2} mol/m^3. Answer: {ret} s.")

    return ret


def second_order_conv_A_plus_B(k_TST, rxn_time, conc1, conc2):
    """
    ln([A]/[B]) = k_TST * ([A]_0 - [B]_0) * time + ln([A]_0/[B]_0)
    ln((A0-x)/(B0-x)) = k_TST * (A0 - B0) * time + ln(A0/B0)
    """

    A0, B0 = min(conc1, conc2), max(conc1, conc2)
    left = k_TST * (A0 - B0) * rxn_time + math.log(A0 / B0)  # ln((A0-x)/(B0-x))
    after_exp = math.exp(left)  # (A0-x)/(B0-x)
    x = (after_exp * B0 - A0) / (after_exp - 1)
    conv = x / A0
    print(f"Calculate conv from second order kinetics.\n"
          f"    Rate constant: {k_TST} m^3·mol^-1·s^-1, time: {rxn_time} s, concentrations: {conc1}, {conc2} mol/m^3. Answer: {conv}.")
    return conv


def second_order_k_TST_A_plus_B(conv, rxn_time, conc1, conc2):
    """
    ln([A]/[B]) = k_TST * ([A]_0 - [B]_0) * time + ln([A]_0/[B]_0)
    ln(A/B) - ln(A0/B0) = k_TST * (A0 - B0) * time
    (ln(A/B) - ln(A0/B0))/time/(A0-B0) = k_TST
    """

    A0, B0 = min(conc1, conc2), max(conc1, conc2)
    A = A0 - A0 * conv
    B = B0 - A0 * conv
    ret = (math.log(A / B) - math.log(A0 / B0)) / rxn_time / (A0 - B0)
    print(f"Calculate k from A+B second order kinetics.\n"
          f"    Conversion: {conv}, time: {rxn_time} s, concentrations: {conc1}, {conc2} mol/m^3. Answer: {ret} m3·mol-1·s-1")
    return ret

# print(solve_for_T(math.log(2)/(8*3600),0,1,118700))

# print(second_order_conv_A_plus_A(0.89/1000,2.50E4,4.5E-2))
# print(second_order_reaction_time_A_plus_A(0.89/1000,0.5,4.5E-2))

# print(get_k_TST(1,1,298,15000))
# print(second_order_reaction_time_A_plus_B(356590343,0.451,0.5E3,1.2E3))
