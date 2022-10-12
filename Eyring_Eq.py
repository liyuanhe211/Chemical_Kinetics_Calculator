# -*- coding: utf-8 -*-

# TODO 写clear每个输入框的按钮（已经放了，但是没功能）

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
from datetime import datetime
from collections import OrderedDict

os.environ["QT_SCALE_FACTOR_ROUNDING_POLICY"] = "Floor"
from PyQt5 import Qt, uic
from PIL import Image, ImageDraw, ImageEnhance

from Python_Lib.My_Lib_PyQt import *
from Lib import *

if not Qt.QApplication.instance():
    Application = Qt.QApplication(sys.argv)
    if platform.system() == 'Windows':
        import ctypes

        Windows_DPI_ratio, PyQt_scaling_ratio = set_Windows_scaling_factor_env_var()

        del Application
        Application = Qt.QApplication(sys.argv)
        APPID = 'LYH.EyringEq.0.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APPID)
        Application.setWindowIcon(Qt.QIcon('UI/Eyring_Eq.png'))
        print('If there is a warning above starts with "libpng", ignore that.')

if __name__ == '__main__':
    pyqt_ui_compile('Eyring_Eq.py')
    from UI.Eyring_Eq import Ui_Eyring_Eq


def evaluate_expression(expression: str):
    expression = expression.replace(' × 10^', 'E')
    try:
        ret = eval(expression)
        if is_float(ret):
            return ret
    except Exception:
        return None


class myWidget(Ui_Eyring_Eq, Qt.QWidget, Qt_Widget_Common_Functions):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(460)
        self.setMinimumHeight(336)
        connect_once(self.unimolecular_radioButton, self.unimolecular_selected)
        connect_once(self.bimolecular_AA_radioButton, self.bimolecular_AA_selected)
        connect_once(self.bimolecular_AB_radioButton, self.bimolecular_AB_selected)
        connect_once(self.reset_all_pushButton, self.reset_all)
        connect_once(self.calculate_pushButton, self.calc)

        connect_once(self.conversion_lineEdit, self.check_fill_status)
        connect_once(self.total_time_lineEdit, self.check_fill_status)
        connect_once(self.temp_lineEdit, self.check_fill_status)
        connect_once(self.G_neq_lineEdit, self.check_fill_status)
        connect_once(self.kTST_lineEdit, self.check_fill_status)
        connect_once(self.conc2_lineEdit, self.check_fill_status)
        connect_once(self.conc1_lineEdit, self.check_fill_status)
        connect_once(self.sigma_lineEdit, self.check_fill_status)
        connect_once(self.unimolecular_radioButton, self.check_fill_status)
        connect_once(self.bimolecular_AA_radioButton, self.check_fill_status)
        connect_once(self.bimolecular_AB_radioButton, self.check_fill_status)
        connect_once(self.total_time_lineEdit, self.smart_display_total_time)

        connect_once(self.temp_lineEdit, self.clear_kTST)
        connect_once(self.G_neq_lineEdit, self.clear_kTST)
        connect_once(self.sigma_lineEdit, self.clear_kTST)
        connect_once(self.unimolecular_radioButton, self.clear_kTST)
        connect_once(self.bimolecular_AA_radioButton, self.clear_kTST)
        connect_once(self.bimolecular_AB_radioButton, self.clear_kTST)

        self.clear_conc1_pushButton.hide()
        self.clear_conc2_pushButton.hide()
        self.clear_G_pushButton.hide()
        self.clear_k_pushButton.hide()
        self.clear_T_pushButton.hide()
        self.clear_t_pushButton.hide()
        self.clear_conv_pushButton.hide()
        self.clear_sigma_pushButton.hide()

        self.kTST_is_calculated_marker = "⠀"  # an unicode blank to tell the program that the kTST is calculated, instead of user input.
        self.unimolecular_selected()
        self.check_fill_status()
        self.show()
        self.center_the_widget()
        self.resize(self.minimumSizeHint())

    # def clear_G(self):
    #     self.G_neq_lineEdit.setText("")

    def unimolecular_selected(self):
        self.conc1_lineEdit.setText("")
        self.conc2_lineEdit.setText("")
        self.conc1_lineEdit.setEnabled(False)
        self.conc2_lineEdit.setEnabled(False)
        self.conc1_lineEdit.setFocusPolicy(Qt.Qt.NoFocus)
        self.conc2_lineEdit.setFocusPolicy(Qt.Qt.NoFocus)
        self.kTST_unit_label.setText("<html><head/><body><p>s<span style=\" vertical-align:super;\">-1</span></p></body></html>")

    def bimolecular_AA_selected(self):
        self.conc1_lineEdit.setEnabled(True)
        self.conc1_lineEdit.setFocusPolicy(Qt.Qt.StrongFocus)
        self.conc2_lineEdit.setEnabled(False)
        self.conc2_lineEdit.setFocusPolicy(Qt.Qt.NoFocus)
        self.conc2_lineEdit.setText("")
        self.kTST_unit_label.setText(
            "<html><head/><body><p>M<span style=\" vertical-align:super;\">-1</span>·s<span style=\" vertical-align:super;\">-1</span></p></body></html>")

    def bimolecular_AB_selected(self):
        self.conc1_lineEdit.setEnabled(True)
        self.conc1_lineEdit.setFocusPolicy(Qt.Qt.StrongFocus)
        self.conc2_lineEdit.setEnabled(True)
        self.conc2_lineEdit.setFocusPolicy(Qt.Qt.StrongFocus)
        self.kTST_unit_label.setText(
            "<html><head/><body><p>M<span style=\" vertical-align:super;\">-1</span>·s<span style=\" vertical-align:super;\">-1</span></p></body></html>")

    def reset_all(self):
        self.G_neq_lineEdit.setText("")
        self.temp_lineEdit.setText("")
        self.conc1_lineEdit.setText("")
        self.conc2_lineEdit.setText("")
        self.sigma_lineEdit.setText("1")
        self.total_time_lineEdit.setText("")
        self.conversion_lineEdit.setText("98")
        # self.unimolecular_radioButton.click()

    def clear_kTST(self):
        if self.kTST_lineEdit.text().startswith(self.kTST_is_calculated_marker):
            self.kTST_lineEdit.setText("")

    def smart_display_total_time(self):
        if self.data["t"] and self.data["t"] > 60:
            self.total_time_display_label.setText("= " + smart_print_time(self.data["t"]))
        else:
            self.total_time_display_label.setText("")

    def set_kTST_line_edit(self, kTST):
        if self.unimolecular_radioButton.isChecked():
            self.kTST_lineEdit.setText(self.kTST_is_calculated_marker + smart_format_float(kTST))
        else:
            self.kTST_lineEdit.setText(self.kTST_is_calculated_marker + smart_format_float(kTST * 1000))

    def check_fill_status(self):
        self.data = {}
        self.data["G"] = evaluate_expression(self.G_neq_lineEdit.text())
        if self.data['G'] is not None:
            self.data['G'] *= 1000  # kJ-> J
        self.data["T"] = evaluate_expression(self.temp_lineEdit.text())
        if self.data['T'] is not None:
            self.data['T'] += 273
        self.data["c1"] = evaluate_expression(self.conc1_lineEdit.text())
        if self.data['c1'] is not None:
            self.data['c1'] *= 1000  # mol/L -> mol/m^3
        self.data["c2"] = evaluate_expression(self.conc2_lineEdit.text())
        if self.data['c2'] is not None:
            self.data['c2'] *= 1000  # mol/L -> mol/m^3
        self.data["t"] = evaluate_expression(self.total_time_lineEdit.text())
        self.data["conv"] = evaluate_expression(self.conversion_lineEdit.text())
        if self.data['conv'] is not None:
            self.data['conv'] /= 100  # percent to number
        if self.kTST_lineEdit.text().startswith(self.kTST_is_calculated_marker):
            self.data['kTST'] = None
        else:
            self.data['kTST'] = evaluate_expression(self.kTST_lineEdit.text())
            if not self.unimolecular_radioButton.isChecked() and self.data['kTST']:
                self.data['kTST'] /= 1000  # L/mol·s --> m3/mol·s
        self.data["σ"] = evaluate_expression(self.sigma_lineEdit.text())
        self.is_None = set([key for key, value in self.data.items() if value is None])
        if self.unimolecular_radioButton.isChecked():
            try:
                self.is_None.remove("c2")
                self.is_None.remove("c1")
            except KeyError:
                pass
        elif self.bimolecular_AA_radioButton.isChecked():
            try:
                self.is_None.remove("c2")
            except KeyError:
                pass
        allowed_missing_situations = [["G", 'kTST'],
                                      ["T", 'kTST'],
                                      ["t", 'kTST'],
                                      ["conv", 'kTST'],
                                      ["G", 't'],
                                      ["G", 'conv'],
                                      ["T", 't'],
                                      ["T", 'conv']]
        allowed = any([set(x) == self.is_None for x in allowed_missing_situations])
        self.calculate_pushButton.setEnabled(allowed)

    def calc(self):
        if self.unimolecular_radioButton.isChecked():
            Δn = 0

            def k_from_kinetics(conv, time, conc1=None, conc2=None):
                return first_order_k_TST(conv, time)

            def t_from_kinetics(kTST, conv, conc1=None, conc2=None):
                return first_order_reaction_time(kTST, conv)

            def conv_from_kinetics(kTST, time, conc1=None, conc2=None):
                return first_order_conversion(kTST, time)

        elif self.bimolecular_AA_radioButton.isChecked():
            print("haha1")
            Δn = 1

            def k_from_kinetics(conv, time, conc1, conc2=None):
                return second_order_k_TST_A_plus_A(conv, time, conc1)

            def t_from_kinetics(kTST, conv, conc1, conc2=None):
                return second_order_reaction_time_A_plus_A(kTST, conv, conc1)

            def conv_from_kinetics(kTST, time, conc1, conc2=None):
                return second_order_conv_A_plus_A(kTST, time, conc1)

        elif self.bimolecular_AB_radioButton.isChecked():
            Δn = 1

            def k_from_kinetics(conv, time, conc1, conc2):
                if conc1 == conc2:
                    return second_order_k_TST_A_plus_A(conv, time, conc1)
                else:
                    return second_order_k_TST_A_plus_B(conv, time, conc1, conc2)

            def t_from_kinetics(kTST, conv, conc1, conc2):
                if conc1 == conc2:
                    return second_order_reaction_time_A_plus_A(kTST, conv, conc1)
                else:
                    return second_order_reaction_time_A_plus_B(kTST, conv, conc1, conc2)

            def conv_from_kinetics(kTST, time, conc1, conc2):
                if conc1 == conc2:
                    return second_order_conv_A_plus_A(kTST, time, conc1)
                else:
                    return second_order_conv_A_plus_B(kTST, time, conc1, conc2)

        # print(Δn)

        G, T, c1, c2, t, conv, σ, kTST = [self.data[key] for key in ["G", "T", "c1", "c2", "t", "conv", "σ", 'kTST']]

        # 知道动力学，从动力学逆推kTST
        if "t" not in self.is_None and 'conv' not in self.is_None:
            kTST = k_from_kinetics(conv, t, c1, c2)
            self.set_kTST_line_edit(kTST)

        if kTST:
            if "G" in self.is_None:  # 知道G不知道T
                G = solve_for_ΔG(kTST, Δn, σ, T)
                self.G_neq_lineEdit.setText(smart_format_float(G / 1000, precision=4))
            elif "T" in self.is_None:  # 知道T不知道G
                T = solve_for_T(kTST, Δn, σ, G)
                self.temp_lineEdit.setText(smart_format_float(T - 273.15, precision=2, scientific_notation_limit=6))

        # 不知道动力学，从kTST算时间、转化率
        if "G" not in self.is_None and "T" not in self.is_None:
            print(f"Calculating rate constant from TST.\n    Δn: {Δn}, σ: {σ}, T: {T} K, ΔG: {G} J/mol.")
            kTST = get_k_TST(Δn, σ, T, G)
            self.set_kTST_line_edit(kTST)
            if "t" in self.is_None:
                t = t_from_kinetics(kTST, conv, c1, c2)
                self.total_time_lineEdit.setText(smart_format_float(t))
            elif 'conv' in self.is_None:
                conv = conv_from_kinetics(kTST, t, c1, c2)
                self.conversion_lineEdit.setText(smart_format_float(conv * 100))

        print("---------------------------------\n\n")


if __name__ == '__main__':
    my_Qt_Program = myWidget()
    my_Qt_Program.show()
    sys.exit(Application.exec_())

""" 
Verification cases：

A -> P
G = 118.7 kJ/mol
time = 8*3600 s
6 half life
T = 370 k = 97 oC
k = 0.000134
--------------------------
A -> P
G = 96.7 kJ/mol
T = 298 K
6 half life
time = 59773 s
--------------------------
A -> P
T = 90 + 273 k
time = 15*60 s
6 half life
G = 105.725
--------------------------
A+B -> P

T = 298 k
conc1 = 0.5 mol/L
conc2 = 1.2 mol/L
G = 15 kJ/mol
kTST = 3.566e+11 s^-1 M^-1

t = 3.93E-13 s
conv = 15%

t = 1.39E-11 s
conv = 98.2%
--------------------------

A+A -> P
conc1 = 4.5E-5
kTST = 0.89 M-1s-1
conv=50%
time = 2.5E4 s

T = 25 oC
G = 81195 J/mol


"""
