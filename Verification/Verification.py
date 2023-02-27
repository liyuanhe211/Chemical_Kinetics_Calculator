# -*- coding: utf-8 -*-
"""
A module to test the GUI with known cases, iterating through all possible unknowns and units for a certain case
"""
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

import pathlib

parent_path = str(pathlib.Path(__file__).parent.parent.resolve())
sys.path.insert(0, parent_path)
os.chdir(parent_path)

from Python_Lib.My_Lib_PyQt6 import *
import Eyring_Eq
from numbers import Real

test_cases = [
    {
        "mode": "AB",
        "T": 25,
        "conc1": 0.5,
        "conc2": 1.2,
        "G": 15,
        "kTST": 3.566E11,
        "t": 3.93E-13,
        "conv": 15
    },
    {
        "mode": "AA",
        "T": 25,
        "conc1": 4.5E-5,
        "G": 81.195,
        "kTST": 0.89,
        "t": 2.5E4,
        "conv": 50
    },
    {
        "mode": "AB",
        "T": 25,
        "conc1": 4.5E-5,
        "conc2": 4.5E-5,
        "G": 81.195,
        "kTST": 0.89,
        "t": 2.5E4,
        "conv": 50
    },
    {
        "mode": "AB",
        "T": 25,
        "conc1": 0.5,
        "conc2": 1.2,
        "G": 15,
        "kTST": 3.566E11,
        "t": 1.39E-11,
        "conv": 98.2
    },
    {
        "mode": "AB",
        "T": 25,
        "conc1": 1.2,
        "conc2": 0.5,
        "G": 15,
        "kTST": 3.566E11,
        "t": 1.39E-11,
        "conv": 98.2
    },
    {
        "mode": "Acat",
        "T": 25,
        "conc2": 10,
        "G": 81.19,
        "kTST": 0.892,
        "t": 0.0777,
        "conv": 50
    },
    {
        "mode": "A",
        "T": 97,
        "G": 118.7,
        "kTST": 0.000134,
        "t": 8 * 3600,
        "conv": 98
    },
    {
        "mode": "A",
        "T": 25,
        "G": 96.7,
        "kTST": 6.9579118707081440415301357303571e-5,
        "t": 59773,
        "conv": 98.5
    },
    {
        "mode": "A",
        "T": 90,
        "G": 105.725,
        "kTST": 0.00462098120373296872944821414305,
        "t": 15 * 60,
        "conv": 98.5,
    },
    {
        "mode": "A",
        "T": 25,
        "G": 73.27,
        "kTST": 0.891,
        "t": .777,
        "conv": 50,
    }
]

# for name in ["mode", "T", "conc1", "conc2", "G", "kTST", "t", "conv"]:
#     for case in test_cases:
#         print(case.get(name,""),end=';')
#     print()


app = Eyring_Eq.Application
self = Eyring_Eq.myWidget()


def run_unknown_combinations(test_case: Dict[str, str or Real]):
    print("Testing...")
    UNKNOWN_COMBINATIONS = [["G", 'kTST'],
                            ["T", 'kTST'],
                            ["t", 'kTST'],
                            ["conv", 'kTST'],
                            ["G", 't'],
                            ["G", 'conv'],
                            ["T", 't'],
                            ["T", 'conv']]

    for unknowns in UNKNOWN_COMBINATIONS:
        energy_units = ("kJ/mol", "kcal/mol", "eV")
        time_units = ("s", "min", "h", "d", "year")
        for energy_unit in energy_units:
            for time_unit in time_units:

                test_input = copy.deepcopy(test_case)
                if energy_unit == 'kcal/mol':
                    test_input['G'] /= kcal__kJ
                elif energy_unit == 'eV':
                    test_input['G'] /= eV__kJ
                if time_unit == 'min':
                    test_input['t'] /= 60
                elif time_unit == 'h':
                    test_input['t'] /= 3600
                elif time_unit == 'd':
                    test_input['t'] /= 86400
                elif time_unit == 'year':
                    test_input['t'] /= (86400 * 365)

                correct_answers = []
                for unknown in unknowns:
                    correct_answers.append(test_input.pop(unknown))
                given_answer = self.automation(test_input, (energy_unit, time_unit), unknowns, redirect_sys_output=True)

                def acceptable(ref: Real, answer: str, marker):
                    # This is not a space.
                    # This is an unicode blank to tell the program that the kTST is calculated, instead of user input.
                    kTST_is_calculated_marker = "⠀"

                    answer = answer.strip(kTST_is_calculated_marker)
                    if answer in [smart_format_float(ref), smart_format_float(ref, 4), smart_format_float(ref, 3, 6)]:
                        return ""
                    answer = float(answer.replace(' × 10^', 'E'))
                    if 0.98 < ref / answer < 1.02:
                        return ""
                    return f"{marker}: {ref}  {answer}"

                compare_1 = acceptable(correct_answers[0], given_answer[0], unknowns[0])
                compare_2 = acceptable(correct_answers[1], given_answer[1], unknowns[1])
                if compare_1 or compare_2:
                    print(compare_1, "|", compare_2)

    print("Finished.")


if __name__ == '__main__':
    # precalculated test cases, the program run through every case, and for each case run through every unknown scenario
    # unit as shown in program default

    for test_case in test_cases:
        print('---------------------------')
        print(test_case)
        run_unknown_combinations(test_case)

    # sys.exit(Eyring_Eq.Application.exec_())

# run_test_case(
#     {
#         "mode": "AB",
#         "T": 298,
#         "conc1": 0.5,
#         "conc2": 1.2,
#         "G": 15,
#         "t": 3.93E-13,
#     },
#     ['kTST', 'conv'])

sys.exit(app.exec())
