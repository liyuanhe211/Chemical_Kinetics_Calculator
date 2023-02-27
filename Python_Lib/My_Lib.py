# -*- coding: utf-8 -*-
__author__ = 'LiYuanhe'

import sys
import os
import re
import string
import copy
import math
from collections import OrderedDict

import pathlib

Python_Lib_path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(Python_Lib_path)
from My_Lib_Stock import *

def video_duration_s(filename):
    import cv2
    video = cv2.VideoCapture(filename)

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # print(filename,fps,frame_count)
    assert fps, filename
    return frame_count / fps

def get_image_size(image_file):
    """
    read an image file, return (width, height) of the image file
    :param image_file:
    :return:
    """
    from PIL import Image
    return Image.open(image_file).size


def screen_capture(output_filename):
    import pyautogui
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(output_filename)

def interpolation_with_grouping(Xs, Ys, kind):
    """
    When X have duplicate values, interp1d fails.
    It is averaged so to be as an single value function
    """
    from scipy.interpolate import interp1d
    from statistics import mean
    from itertools import groupby

    process_XYs = list(zip(Xs, Ys))
    process_XYs.sort(key=lambda x: x[0])
    grouper = groupby(process_XYs, key=lambda x: x[0])
    process_XYs = [[x, mean(yi[1] for yi in y)] for x, y in grouper]
    interp1d_X = [x[0] for x in process_XYs]
    interp1d_Y = [x[1] for x in process_XYs]

    # print(len(interp1d_X))
    # print(len(set(interp1d_X)))

    return interp1d(interp1d_X, interp1d_Y, kind=kind)


def hide_cwd_window():
    import ctypes
    import os
    import win32process

    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        ctypes.windll.user32.ShowWindow(hwnd, 0)
        ctypes.windll.kernel32.CloseHandle(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        os.system('taskkill /PID ' + str(pid) + ' /f')


def toggle_layout(layout, hide=-1, show=-1):
    """
    Hide (or show) all elements in layout
    :param layout:
    :param hide: to hide layout
    :param show: to show layout
    :return:
    """

    for i in reversed(range(layout.count())):
        assert hide != -1 or show != -1
        assert isinstance(hide, bool) or isinstance(show, bool)

        if isinstance(show, bool):
            hide = not show

        if hide:
            if layout.itemAt(i).widget():
                layout.itemAt(i).widget().hide()
        else:
            if layout.itemAt(i).widget():
                layout.itemAt(i).widget().show()


class SSH_Account:
    def __init__(self, input_str: str):
        """
        :param input_str: name 100.100.101.123:1823 username password
                        or with ssh private key name 100.100.101.123:1234 username E:\path_to_key_file\keyfile.openssh
        """
        input_str = input_str.strip().split(" ")
        self.tag = input_str[0]
        self.ip_port = input_str[1]
        self.ip, self.port = self.ip_port.split(":")

        try:
            self.port = int(self.port)
        except:
            self.port = 22

        self.username = input_str[2]
        self.password = input_str[3]

    def __str__(self):
        return self.username + ' @ ' + self.tag


def download_sftp_file(ssh_account: SSH_Account, remote_filepath, local_filepath, transport_object=None, sftp_object=None):
    # 产生一个随机的临时文件，然后改名为想要的文件名，某种程度上保证原子性
    remove_append = filename_class(local_filepath).only_remove_append
    append = filename_class(local_filepath).append

    local_temp_filepath = remove_append + "_TEMP_For_atomicity." + append

    import paramiko
    if not transport_object:
        transport = paramiko.Transport((ssh_account.ip, ssh_account.port))
        transport.connect(username=ssh_account.username, password=ssh_account.password)
    else:
        transport = transport_object

    if not sftp_object:
        sftp = paramiko.SFTPClient.from_transport(transport)
    else:
        sftp = sftp_object

    ssh_for_homedir = paramiko.SSHClient()
    ssh_for_homedir.load_system_host_keys()
    ssh_for_homedir.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_for_homedir.connect(ssh_account.ip, ssh_account.port, username=ssh_account.username, password=ssh_account.password)

    stdin, stdout, stderr = ssh_for_homedir.exec_command("echo " + remote_filepath)
    remote_filepath = stdout.read().decode('utf-8').strip()

    sftp.get(remote_filepath, local_temp_filepath)

    if os.path.isfile(local_filepath):
        os.remove(local_filepath)
    os.rename(local_temp_filepath, local_filepath)

    if not sftp_object:
        sftp.close()

    ssh_for_homedir.close()


def find_range_for_certain_percentage(data, percentage=80, offset=0):
    """
    try to find the smallest data range, where it can cover certain percentage of the data
    :param data: a list of numbers, or any shape of numpy array, which will be flatened
    :param offset:a number, if it is 0.1, then the color map will be shifted up for 10% of max(Z)-min(Z)
    :return: a 2-tuple, the desired smallest range
    """
    import numpy as np
    data = np.array(data)
    data_dist = max(data) - min(data)
    data = np.sort(data, axis=None)
    data_count = data.size
    target_count = math.ceil(data_count * percentage / 100)
    ranges = []
    for i in range(0, data_count - target_count + 1):
        ranges.append((data[i], data[i + target_count - 1]))
    ranges.sort(key=lambda x: x[1] - x[0])
    ret = list(ranges[0])
    print(ret)
    ret[0] = ret[0] + data_dist * offset
    ret[1] = ret[1] + data_dist * offset
    print(ret)
    return ret


def Chronyk_new(input_time: str):  # chronyk will give a 1 day less result when wap arround time string
    from chronyk import Chronyk
    if isinstance(input_time, float):
        return Chronyk(input_time)
    elif isinstance(input_time, str):
        return Chronyk(Chronyk(input_time).timestamp() + 86400)


def remove_forbidden_char_from_filename(filename):
    chars = r'<>:"/\|?*'
    for char in chars:
        filename = filename.replace(char, '_')
    return filename


def quote_url(url):
    from urllib import parse
    return parse.quote(url, safe=':?/=')


# def get_response_header_using_cookie(url):
#     import requests
#     r = requests.get(url)
#     header = r.headers
#     # cookie = r.cookies
#     r = requests.get(url,cookies = cookie)
#     print(r.headers)

def open_url_with_chrome(url):
    import webbrowser
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open_new_tab(url)


def open_phantomJS(url, use_chrome=False):
    os.environ["PATH"] += r';D:\常用程序\Chrome;D:\常用程序\phantomjs-2.1.1-windows\bin'
    if os.path.isfile('PhantomJS_Path.txt'):
        with open('PhantomJS_Path.txt') as PhantomJS_Path_file:
            os.environ["PATH"] += ";" + PhantomJS_Path_file.read().strip()

    from selenium import webdriver

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    if not use_chrome:
        # Connect_to_PhantomJS
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap[
            "phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        test_driver = webdriver.PhantomJS(desired_capabilities=dcap)

    if use_chrome:
        test_driver = webdriver.Chrome()

    test_driver.get(url)
    return test_driver


def urlopen_inf_retry(url, prettify=True, use_cookie=False, retry_limit=100, opener=None, timeout=60, print_out=True):
    from bs4 import BeautifulSoup

    from http.cookiejar import CookieJar
    import urllib
    from urllib import request
    import socket

    html = None

    def request_page(requrest_url, request_page_opener, request_page_timeout=60):
        if use_cookie:
            if not request_page_opener:
                request_page_opener = request.build_opener(request.HTTPCookieProcessor(CookieJar()))
            return request_page_opener.open(requrest_url, timeout=request_page_timeout)
        else:
            req = request.Request(requrest_url, headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"})
            return request.urlopen(req, timeout=request_page_timeout)

    fail = True
    retry_count = 1
    while fail and retry_count <= retry_limit:
        if print_out:
            print("Requesting:", url, end='\t')
        try:
            html = request_page(url, opener, request_page_timeout=timeout).read()
            fail = False
            if print_out:
                print("Request Finished.")
        except (socket.gaierror, urllib.error.URLError, ConnectionResetError, TimeoutError, socket.timeout, UnboundLocalError) as e:
            if print_out:
                print('\nURL open failure. Retrying... ' + str(retry_count) + '/' + str(retry_limit), e)
            retry_count += 1
            import time
            time.sleep(2)

    if not html:
        return ""
    if prettify:
        html = BeautifulSoup(html, "lxml").prettify()
        return BeautifulSoup(html, "lxml")
    else:
        return html


def match_attr_bs4(bs_object, key, value, match_full=False):
    # time.sleep(1)
    if not match_full:
        if bs_object.get(key):
            if value in bs_object[key]:
                return True
    else:
        if bs_object.get(key):
            target = bs_object[key]
            target = " ".join([" ".join(x.split()) for x in target])
            value = " ".join(value.split)
            if target == value:
                return True
    return False


def open_tab(url):
    import webbrowser
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"))
    browser = webbrowser.get('brave')
    browser.open_new_tab(url)


def get_canonical_smiles(original_smiles):
    import subprocess
    if not original_smiles:
        return ""

    indigo_path = os.path.join(filename_class(os.path.realpath(__file__)).path, 'indigo-cano.exe').replace('/', '\\')

    print("Calling", ' '.join([indigo_path, '-', original_smiles]))

    try:
        ret = subprocess.check_output([indigo_path, '-', original_smiles])
    except subprocess.CalledProcessError:
        print("Indigo SMILES Bug Detected:", original_smiles)
        try:
            ret = subprocess.check_output(" ".join(['"' + indigo_path + '"', '-', '"' + original_smiles + '"', '-smiles', '-no-arom']), shell=True)
        except subprocess.CalledProcessError:
            return ""

    return ret.decode('utf-8').strip()

    # if not original_smiles:
    #     return ""
    #
    # from indigo.indigo import Indigo
    # indigo = Indigo()
    # try:
    #     mol = indigo.loadMolecule(original_smiles)
    # except:
    #     print("Ineffective SMILES:",original_smiles)
    #     return ""
    #
    # mol.aromatize()
    # try:
    #     ret = mol.canonicalSmiles() #有时有问题
    # except:
    #     ret = original_smiles
    #     print("Indigo SMILES Bug Detected:",original_smiles)
    #
    # # print("Canonicalization time","{:.2f}".format(time.time()-t1))
    #
    # return ret


def load_xlsx_as_list(filename, sheet=0, column_as_inner_list=False):
    import pyexcel
    if isinstance(sheet, int):
        excel_book_dict = pyexcel.get_book_dict(file_name=filename)
        excel_object = excel_book_dict[list(excel_book_dict.keys())[sheet]]
    else:
        excel_object = pyexcel.get_book_dict(file_name=filename)[sheet]

    if not column_as_inner_list:
        return excel_object

    else:  # 转置
        excel_object = [[r[col] for r in excel_object] for col in range(len(excel_object[0]))]
        for i in excel_object:
            print(i)
        return excel_object

    # for line in scaling_factor_database:
    #     # 储存一个原始的，一个最后的
    #     line['Basis'] = [line['Basis'], unify_basis(line['Basis'])]
    #     line['Method'] = [line['Method'], unify_method(line['Method'])]
    #
    # return scaling_factor_database


def excel_formula(formula: str, *cells):
    if isinstance(cells[0], list):
        cells = cells[0]
    for count, current_cell in enumerate(cells):
        formula = formula.replace('[cell' + str(count + 1) + ']', current_cell)

    return formula


def cell(column_num, row_num):
    # start from 0
    if column_num < 26:
        return chr(ord('A') + column_num) + str(row_num + 1)
    if column_num >= 26:
        return chr(ord('A') + int(column_num / 26) - 1) + chr(ord('A') + column_num % 26) + str(row_num + 1)


def read_xlsx(file, sheet=0, all_sheets=False):
    """

    :param file: A xlsx file
    :param sheet: which sheet to read, using numbers
    :param all_sheets: read all sheet, return an ordered dict, with sheet name as key
    :return: if not all_sheets, return a 2D-list, all sub-list are the same length
    """
    import pyexcel_xlsx
    import json
    data = pyexcel_xlsx.get_data(file, skip_hidden_row_and_column=False)

    if all_sheets:
        import collections
        ret = collections.OrderedDict()
        for key, value in data.items():
            ret[key] = same_length_2d_list(value)
        return ret
    else:
        ret = data[list(data)[sheet]]
        return same_length_2d_list(ret)


def read_csv(file):
    """
    Read a csv file, return a same_length_2D_list
    :return: return a 2D-list, same as the csv file, all sub-list are the same length. If the content is 'floatable', it will be convert to float
    """

    with open(file) as input_file:
        input_file_content = input_file.readlines()

    input_file_content = [x.strip().split(',') for x in input_file_content]
    data = [[(float(y) if is_float(y) else y) for y in x] for x in input_file_content]
    return same_length_2d_list(data)


def read_txt_table(file, separater='\t'):
    data = open(file).readlines()
    data = [x.split(separater) for x in data]
    return same_length_2d_list(data)


def read_txt_and_transpose(file, separater='\t'):
    return transpose_2d_list(read_txt_table(file, separater=separater))


def write_xlsx(filename, list_2D, transpose=False):
    """
    A simple function for writing a 2D list to a xlsx file
    :param filename:
    :param list_2D:
    :param transpose: if False, the outer-layer of list-2D will be rows
    :return:
    """

    import xlsxwriter
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    for row_count, row in enumerate(list_2D):
        for column_count, current_cell in enumerate(row):
            if not transpose:
                worksheet.write(row_count, column_count, current_cell)
            else:
                worksheet.write(column_count, row_count, current_cell)

    workbook.close()


def mix_two_colors(color1, color2, percentage, mixing_order=2):
    """
    :param color1: color in hex, e.g. "00FF00"
    :param color2: color in hex, e.g. "00FF00"
    :param mixing_order:
    :param percentage: if =0, color1, if =1, color2, else, return an interpolation of the color
    :return: a mixed color in hex number
    """
    if mixing_order == 'hsv':
        import colorsys
    if percentage == 0:
        return color1
    if percentage == 1:
        return color2

    color1 = [eval('0x' + x) for x in [color1[0:2], color1[2:4], color1[4:6]]]
    color2 = [eval('0x' + x) for x in [color2[0:2], color2[2:4], color2[4:6]]]

    def mixing(value1, value2, percentage, mixing_order):
        return round((value1 ** mixing_order + (value2 ** mixing_order - value1 ** mixing_order) * percentage) ** (1 / mixing_order))

    def hsv_mixing(color1, color2, percentage):
        color1 = [x / 255 for x in color1]
        color2 = [x / 255 for x in color2]
        color1 = colorsys.rgb_to_hsv(*color1)
        color2 = colorsys.rgb_to_hsv(*color2)
        ret = colorsys.hsv_to_rgb(*[color1[x] + percentage * (color2[x] - color1[x]) for x in range(3)])
        return (round(x * 255) for x in ret)

    if mixing_order == 'hsv':
        ret = hsv_mixing(color1, color2, percentage)
    else:
        ret = [mixing(color1[x], color2[x], percentage, mixing_order) for x in range(3)]

    ret = ''.join('{:02X}'.format(int(round(num))) for num in ret)
    return ret


def color_scale(colors, ref_points, value, mixing_order=2):
    '''
    generate a color scale, extract color for a value
    :param colors: list of colors corresponds to list of ref_points, color in Hex like FFFFFF
    :param ref_points:
    :param value:
    :return:
    '''

    assert sorted(ref_points) == ref_points or sorted(ref_points, reverse=True) == ref_points, 'Color Ref Points need to be in sequence.'
    if sorted(ref_points, reverse=True) == ref_points:
        ref_points = list(reversed(ref_points))
        colors = list(reversed(colors))

    if value < ref_points[0]:
        return colors[0]
    if value > ref_points[-1]:
        return colors[-1]

    for value_count in range(len(ref_points) - 1):
        value1, value2 = ref_points[value_count:value_count + 2]
        if value1 <= value <= value2:
            color1, color2 = colors[value_count:value_count + 2]
            return mix_two_colors(color1, color2, (value - value1) / (value2 - value1), mixing_order=mixing_order)


def angle_of_np_vectors(v1, v2):
    """ Returns the angle in degree between vectors 'v1' and 'v2'::"""
    import numpy as np
    def unit_vector(vector):
        return vector / np.linalg.norm(vector)

    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)) / math.pi * 180


def smiles_from_xyz(input_file):
    import subprocess
    babel_exe = r"C:\Program Files (x86)\OpenBabel-2.3.2\babel.exe"
    assert os.path.isfile(babel_exe), "OpenBabel not found."
    temp_file = r"D:\Gaussian\Temp\temp_xyz_file_for_smiles.smi"

    subprocess.call([babel_exe, '-ixyz', input_file, "-osmi", temp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open(temp_file) as temp_file:
        ret = temp_file.read().split()
        if ret:
            return (get_canonical_smiles(ret[0]))
        else:
            print("SMILES ERROR! Original str:", ret)


def smiles_from_mol2(input_file):
    import subprocess
    babel_exe = r"C:\Program Files (x86)\OpenBabel-2.3.2\babel.exe"
    assert os.path.isfile(babel_exe), "OpenBabel not found."
    temp_file = r"D:\Gaussian\Temp\temp_xyz_file_for_smiles.smi"

    subprocess.call([babel_exe, '-imol2', input_file, "-osmi", temp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open(temp_file) as temp_file:
        ret = temp_file.read().split()
        if ret:
            return (get_canonical_smiles(ret[0]))
        else:
            print("SMILES ERROR! Original str:", ret)


def get_bonds(filename, neighbor_list=False, add_bond="", bond_radii_factor=1.3):
    '''

    :param filename: ALL file format supported by mogli
    :param neighbor_list: is neighbor_list=True, a dict of neighbor list of connection are returned, instead of the standard one {1:[3,4,5], 2:[3,6,7]}
    :param add_bond: a str with the format of "1-2,1-5", atom count start from 0, where a (single) bond will be added if they are not bonded before

    :return: a list of tuple of bonded atoms,no bond order information
            e.g. [(0, 1), (0, 2), (0, 13), (0, 26), (2, 3), (2, 4), (2, 5), (5, 6), (5, 9), (5, 10), (6, 7), (6, 8), (7, 13), (10, 11), (10, 12), (12, 13), (12, 38), (13, 14), (14, 15), (14, 16), (14, 20), (16, 17), (16, 18), (16, 19), (20, 21), (20, 22), (20, 23), (23, 24), (23, 25), (23, 26), (26, 27), (27, 28), (27, 32), (28, 29), (28, 30), (28, 31), (32, 33), (32, 34), (32, 35), (35, 36), (35, 37), (35, 38), (38, 39), (38, 40), (40, 41), (40, 45), (40, 46), (41, 42), (41, 43), (41, 44), (46, 47), (46, 48), (46, 49)]
            
            if neighbor_list is enabled:
            {0: [1, 3, 4], 1: [0, 2, 10], 2: [1], 3: [0], 4: [0, 5, 6], 5: [4], 6: [4, 7, 8], 7: [6], 8: [6, 9, 10], 9: [8], 10: [1, 8, 11], 11: [10, 12, 13, 14], 12: [11], 13: [11], 14: [11, 15], 15: [14, 16, 17, 49], 16: [15], 17: [15, 18, 19, 34], 18: [17], 19: [17, 20, 21, 22], 20: [19], 21: [19], 22: [19, 23, 24, 25], 23: [22], 24: [22], 25: [22, 26, 27, 28], 26: [25], 27: [25], 28: [25, 29, 30, 31], 29: [28], 30: [28], 31: [28, 32, 33, 34], 32: [31], 33: [31], 34: [17, 31, 35, 36], 35: [34, 49], 36: [34, 37, 38, 39], 37: [36], 38: [36], 39: [36, 40, 41, 42], 40: [39], 41: [39], 42: [39, 43, 47, 61], 43: [42, 44, 45, 46], 44: [43], 45: [43], 46: [43], 47: [42, 48, 49, 53], 48: [47], 49: [15, 35, 47, 50], 50: [49, 51], 51: [50, 52, 53], 52: [51], 53: [47, 51, 54, 55], 54: [53], 55: [53, 56, 60, 61], 56: [55, 57, 58, 59], 57: [56], 58: [56], 59: [56], 60: [55], 61: [42, 55, 62], 62: [61]}
    '''

    # convert "1-2,1-5" to [(1,2),(1,5)]
    if not add_bond:
        add_bond = []
    else:
        add_bond = add_bond.split(",")
        new_add_bond = []
        for bond in add_bond:
            bond = bond.split('-')
            bond = [int(x) - 1 for x in bond]
            bond.sort()
            new_add_bond.append(bond)

        add_bond = new_add_bond

    import mogli
    import time
    molecules = mogli.read(filename)
    retry_attempts = 0
    while not molecules:
        print("Mogli reading error, retrying...")
        time.sleep(0.2)
        molecules = mogli.read(filename)
        retry_attempts += 1
        if retry_attempts > 5:
            break

    molecule = molecules[-1]
    molecule.calculate_bonds(param=bond_radii_factor)
    bonds = molecule.bonds
    bonds = [sorted(list(x)) for x in bonds.index_pairs]
    # print(bonds)

    for new_bond in add_bond:
        for existed_bond in bonds:
            if new_bond[0] == existed_bond[0] and new_bond[1] == existed_bond[1]:
                break
        else:
            bonds.append(new_bond)

    bonds = sorted([sorted(list(x)) for x in bonds])
    # print(bonds)

    if neighbor_list:
        atom_count = len(molecule.atomic_numbers)
        ret = {}
        for atom in range(atom_count):
            bonding_to = []
            for bond in bonds:
                if atom in bond:
                    bonding_to.append(bond[0] if bond[0] != atom else bond[1])
            ret[atom] = bonding_to
        return ret

    return bonds


pass

if __name__ == "__main__":
   pass