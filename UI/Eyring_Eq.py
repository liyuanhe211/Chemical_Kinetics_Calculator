# Form implementation generated from reading ui file 'UI/Eyring_Eq.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Eyring_Eq(object):
    def setupUi(self, Eyring_Eq):
        Eyring_Eq.setObjectName("Eyring_Eq")
        Eyring_Eq.resize(620, 402)
        self.verticalLayout = QtWidgets.QVBoxLayout(Eyring_Eq)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.G_neq_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.G_neq_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.G_neq_lineEdit.setFont(font)
        self.G_neq_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.G_neq_lineEdit.setPlaceholderText("")
        self.G_neq_lineEdit.setObjectName("G_neq_lineEdit")
        self.gridLayout.addWidget(self.G_neq_lineEdit, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Eyring_Eq)
        self.label_2.setMinimumSize(QtCore.QSize(67, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.kTST_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.kTST_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.kTST_lineEdit.setFont(font)
        self.kTST_lineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.kTST_lineEdit.setText("")
        self.kTST_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.kTST_lineEdit.setReadOnly(False)
        self.kTST_lineEdit.setPlaceholderText("")
        self.kTST_lineEdit.setObjectName("kTST_lineEdit")
        self.gridLayout.addWidget(self.kTST_lineEdit, 4, 1, 1, 1)
        self.conc1_label = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conc1_label.setFont(font)
        self.conc1_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.conc1_label.setObjectName("conc1_label")
        self.gridLayout.addWidget(self.conc1_label, 1, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)
        self.kTST_unit_label = QtWidgets.QLabel(parent=Eyring_Eq)
        self.kTST_unit_label.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.kTST_unit_label.setFont(font)
        self.kTST_unit_label.setObjectName("kTST_unit_label")
        self.gridLayout.addWidget(self.kTST_unit_label, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.conc1_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.conc1_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conc1_lineEdit.setFont(font)
        self.conc1_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.conc1_lineEdit.setObjectName("conc1_lineEdit")
        self.gridLayout.addWidget(self.conc1_lineEdit, 1, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(224, 224, 224);")
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 4, 5, 1)
        self.conversion_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.conversion_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conversion_lineEdit.setFont(font)
        self.conversion_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.conversion_lineEdit.setObjectName("conversion_lineEdit")
        self.gridLayout.addWidget(self.conversion_lineEdit, 3, 6, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("color: rgb(224, 224, 224);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 8)
        self.temp_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.temp_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.temp_lineEdit.setFont(font)
        self.temp_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.temp_lineEdit.setObjectName("temp_lineEdit")
        self.gridLayout.addWidget(self.temp_lineEdit, 2, 1, 1, 1)
        self.conc1_unit_label = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conc1_unit_label.setFont(font)
        self.conc1_unit_label.setObjectName("conc1_unit_label")
        self.gridLayout.addWidget(self.conc1_unit_label, 1, 7, 1, 1)
        self.total_time_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.total_time_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.total_time_lineEdit.setFont(font)
        self.total_time_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.total_time_lineEdit.setPlaceholderText("")
        self.total_time_lineEdit.setObjectName("total_time_lineEdit")
        self.gridLayout.addWidget(self.total_time_lineEdit, 4, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Eyring_Eq)
        self.label_4.setMinimumSize(QtCore.QSize(67, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 5, 1, 1)
        self.conv_label = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conv_label.setFont(font)
        self.conv_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.conv_label.setObjectName("conv_label")
        self.gridLayout.addWidget(self.conv_label, 3, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 7, 1, 1)
        self.conc2_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.conc2_lineEdit.setEnabled(False)
        self.conc2_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conc2_lineEdit.setFont(font)
        self.conc2_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.conc2_lineEdit.setObjectName("conc2_lineEdit")
        self.gridLayout.addWidget(self.conc2_lineEdit, 2, 6, 1, 1)
        self.conc2_label = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conc2_label.setFont(font)
        self.conc2_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.conc2_label.setObjectName("conc2_label")
        self.gridLayout.addWidget(self.conc2_label, 2, 5, 1, 1)
        self.conc2_unit_label = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.conc2_unit_label.setFont(font)
        self.conc2_unit_label.setObjectName("conc2_unit_label")
        self.gridLayout.addWidget(self.conc2_unit_label, 2, 7, 1, 1)
        self.sigma_lineEdit = QtWidgets.QLineEdit(parent=Eyring_Eq)
        self.sigma_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.sigma_lineEdit.setFont(font)
        self.sigma_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sigma_lineEdit.setObjectName("sigma_lineEdit")
        self.gridLayout.addWidget(self.sigma_lineEdit, 3, 1, 1, 1)
        self.calculate_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.calculate_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.calculate_pushButton.setFont(font)
        self.calculate_pushButton.setObjectName("calculate_pushButton")
        self.gridLayout.addWidget(self.calculate_pushButton, 7, 5, 1, 4)
        self.reset_all_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.reset_all_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.reset_all_pushButton.setFont(font)
        self.reset_all_pushButton.setObjectName("reset_all_pushButton")
        self.gridLayout.addWidget(self.reset_all_pushButton, 7, 0, 1, 4)
        self.clear_G_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_G_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_G_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_G_pushButton.setFont(font)
        self.clear_G_pushButton.setObjectName("clear_G_pushButton")
        self.gridLayout.addWidget(self.clear_G_pushButton, 1, 3, 1, 1)
        self.clear_sigma_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_sigma_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_sigma_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_sigma_pushButton.setFont(font)
        self.clear_sigma_pushButton.setObjectName("clear_sigma_pushButton")
        self.gridLayout.addWidget(self.clear_sigma_pushButton, 3, 3, 1, 1)
        self.clear_k_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_k_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_k_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_k_pushButton.setFont(font)
        self.clear_k_pushButton.setObjectName("clear_k_pushButton")
        self.gridLayout.addWidget(self.clear_k_pushButton, 4, 3, 1, 1)
        self.clear_T_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_T_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_T_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_T_pushButton.setFont(font)
        self.clear_T_pushButton.setObjectName("clear_T_pushButton")
        self.gridLayout.addWidget(self.clear_T_pushButton, 2, 3, 1, 1)
        self.clear_conc1_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_conc1_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_conc1_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_conc1_pushButton.setFont(font)
        self.clear_conc1_pushButton.setObjectName("clear_conc1_pushButton")
        self.gridLayout.addWidget(self.clear_conc1_pushButton, 1, 8, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.unimolecular_radioButton = QtWidgets.QRadioButton(parent=self.groupBox)
        self.unimolecular_radioButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.unimolecular_radioButton.setFont(font)
        self.unimolecular_radioButton.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.unimolecular_radioButton.setChecked(True)
        self.unimolecular_radioButton.setObjectName("unimolecular_radioButton")
        self.horizontalLayout_3.addWidget(self.unimolecular_radioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bimolecular_AA_radioButton = QtWidgets.QRadioButton(parent=self.groupBox)
        self.bimolecular_AA_radioButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.bimolecular_AA_radioButton.setFont(font)
        self.bimolecular_AA_radioButton.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.bimolecular_AA_radioButton.setObjectName("bimolecular_AA_radioButton")
        self.horizontalLayout_3.addWidget(self.bimolecular_AA_radioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.bimolecular_AB_radioButton = QtWidgets.QRadioButton(parent=self.groupBox)
        self.bimolecular_AB_radioButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.bimolecular_AB_radioButton.setFont(font)
        self.bimolecular_AB_radioButton.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.bimolecular_AB_radioButton.setObjectName("bimolecular_AB_radioButton")
        self.horizontalLayout_3.addWidget(self.bimolecular_AB_radioButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.bimolecular_A_Cat_radioButton = QtWidgets.QRadioButton(parent=self.groupBox)
        self.bimolecular_A_Cat_radioButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.bimolecular_A_Cat_radioButton.setFont(font)
        self.bimolecular_A_Cat_radioButton.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.bimolecular_A_Cat_radioButton.setObjectName("bimolecular_A_Cat_radioButton")
        self.horizontalLayout_3.addWidget(self.bimolecular_A_Cat_radioButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 9)
        self.clear_conc2_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_conc2_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_conc2_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_conc2_pushButton.setFont(font)
        self.clear_conc2_pushButton.setObjectName("clear_conc2_pushButton")
        self.gridLayout.addWidget(self.clear_conc2_pushButton, 2, 8, 1, 1)
        self.clear_t_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_t_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_t_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_t_pushButton.setFont(font)
        self.clear_t_pushButton.setObjectName("clear_t_pushButton")
        self.gridLayout.addWidget(self.clear_t_pushButton, 4, 8, 1, 1)
        self.clear_conv_pushButton = QtWidgets.QPushButton(parent=Eyring_Eq)
        self.clear_conv_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_conv_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.clear_conv_pushButton.setFont(font)
        self.clear_conv_pushButton.setObjectName("clear_conv_pushButton")
        self.gridLayout.addWidget(self.clear_conv_pushButton, 3, 8, 1, 1)
        self.total_time_display_label = QtWidgets.QLabel(parent=Eyring_Eq)
        self.total_time_display_label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.total_time_display_label.setFont(font)
        self.total_time_display_label.setText("")
        self.total_time_display_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.total_time_display_label.setObjectName("total_time_display_label")
        self.gridLayout.addWidget(self.total_time_display_label, 5, 5, 1, 3)
        self.energy_unit_comboBox = QtWidgets.QComboBox(parent=Eyring_Eq)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.energy_unit_comboBox.sizePolicy().hasHeightForWidth())
        self.energy_unit_comboBox.setSizePolicy(sizePolicy)
        self.energy_unit_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.energy_unit_comboBox.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.energy_unit_comboBox.setFont(font)
        self.energy_unit_comboBox.setObjectName("energy_unit_comboBox")
        self.energy_unit_comboBox.addItem("")
        self.energy_unit_comboBox.addItem("")
        self.energy_unit_comboBox.addItem("")
        self.gridLayout.addWidget(self.energy_unit_comboBox, 1, 2, 1, 1)
        self.time_unit_comboBox = QtWidgets.QComboBox(parent=Eyring_Eq)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_unit_comboBox.sizePolicy().hasHeightForWidth())
        self.time_unit_comboBox.setSizePolicy(sizePolicy)
        self.time_unit_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.time_unit_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.time_unit_comboBox.setFont(font)
        self.time_unit_comboBox.setObjectName("time_unit_comboBox")
        self.time_unit_comboBox.addItem("")
        self.time_unit_comboBox.addItem("")
        self.time_unit_comboBox.addItem("")
        self.time_unit_comboBox.addItem("")
        self.time_unit_comboBox.addItem("")
        self.gridLayout.addWidget(self.time_unit_comboBox, 4, 7, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("color: rgb(224, 224, 224);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.status_label_2 = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.status_label_2.setFont(font)
        self.status_label_2.setObjectName("status_label_2")
        self.verticalLayout.addWidget(self.status_label_2)
        self.status_label_3 = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.status_label_3.setFont(font)
        self.status_label_3.setObjectName("status_label_3")
        self.verticalLayout.addWidget(self.status_label_3)
        self.status_label_5 = QtWidgets.QLabel(parent=Eyring_Eq)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.status_label_5.setFont(font)
        self.status_label_5.setObjectName("status_label_5")
        self.verticalLayout.addWidget(self.status_label_5)

        self.retranslateUi(Eyring_Eq)
        self.energy_unit_comboBox.setCurrentIndex(0)
        self.time_unit_comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Eyring_Eq)
        Eyring_Eq.setTabOrder(self.G_neq_lineEdit, self.temp_lineEdit)
        Eyring_Eq.setTabOrder(self.temp_lineEdit, self.kTST_lineEdit)
        Eyring_Eq.setTabOrder(self.kTST_lineEdit, self.conc1_lineEdit)
        Eyring_Eq.setTabOrder(self.conc1_lineEdit, self.conc2_lineEdit)
        Eyring_Eq.setTabOrder(self.conc2_lineEdit, self.conversion_lineEdit)
        Eyring_Eq.setTabOrder(self.conversion_lineEdit, self.total_time_lineEdit)
        Eyring_Eq.setTabOrder(self.total_time_lineEdit, self.calculate_pushButton)
        Eyring_Eq.setTabOrder(self.calculate_pushButton, self.reset_all_pushButton)
        Eyring_Eq.setTabOrder(self.reset_all_pushButton, self.sigma_lineEdit)
        Eyring_Eq.setTabOrder(self.sigma_lineEdit, self.energy_unit_comboBox)
        Eyring_Eq.setTabOrder(self.energy_unit_comboBox, self.time_unit_comboBox)
        Eyring_Eq.setTabOrder(self.time_unit_comboBox, self.clear_G_pushButton)
        Eyring_Eq.setTabOrder(self.clear_G_pushButton, self.clear_T_pushButton)
        Eyring_Eq.setTabOrder(self.clear_T_pushButton, self.clear_k_pushButton)
        Eyring_Eq.setTabOrder(self.clear_k_pushButton, self.clear_conc1_pushButton)
        Eyring_Eq.setTabOrder(self.clear_conc1_pushButton, self.clear_conc2_pushButton)
        Eyring_Eq.setTabOrder(self.clear_conc2_pushButton, self.clear_conv_pushButton)
        Eyring_Eq.setTabOrder(self.clear_conv_pushButton, self.clear_t_pushButton)
        Eyring_Eq.setTabOrder(self.clear_t_pushButton, self.clear_sigma_pushButton)

    def retranslateUi(self, Eyring_Eq):
        _translate = QtCore.QCoreApplication.translate
        Eyring_Eq.setWindowTitle(_translate("Eyring_Eq", "Eyring Equation Solver by LYH"))
        self.label_15.setText(_translate("Eyring_Eq", "σ"))
        self.label_2.setText(_translate("Eyring_Eq", "Temp."))
        self.conc1_label.setText(_translate("Eyring_Eq", "Conc. A"))
        self.label_9.setText(_translate("Eyring_Eq", "°C"))
        self.kTST_unit_label.setText(_translate("Eyring_Eq", "<html><head/><body><p>M<span style=\" vertical-align:super;\">-1</span>·s<span style=\" vertical-align:super;\">-1</span></p></body></html>"))
        self.label.setText(_translate("Eyring_Eq", "<html><head/><body><p>Δ<span style=\" font-style:italic;\">G</span><span style=\" font-style:italic; vertical-align:super;\">≠ </span></p></body></html>"))
        self.label_6.setText(_translate("Eyring_Eq", "<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" vertical-align:sub;\">TST</span></p></body></html>"))
        self.conversion_lineEdit.setText(_translate("Eyring_Eq", "98"))
        self.conc1_unit_label.setText(_translate("Eyring_Eq", "mol/L"))
        self.label_4.setText(_translate("Eyring_Eq", "Rxn Time"))
        self.conv_label.setText(_translate("Eyring_Eq", "Conv."))
        self.label_12.setText(_translate("Eyring_Eq", "%"))
        self.conc2_label.setText(_translate("Eyring_Eq", "Conc. B"))
        self.conc2_unit_label.setText(_translate("Eyring_Eq", "mol/L"))
        self.sigma_lineEdit.setText(_translate("Eyring_Eq", "1"))
        self.calculate_pushButton.setText(_translate("Eyring_Eq", "Calculate"))
        self.calculate_pushButton.setShortcut(_translate("Eyring_Eq", "Ctrl+Shift+C"))
        self.reset_all_pushButton.setText(_translate("Eyring_Eq", "Reset All"))
        self.reset_all_pushButton.setShortcut(_translate("Eyring_Eq", "Ctrl+Shift+R"))
        self.clear_G_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.clear_sigma_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.clear_k_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.clear_T_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.clear_conc1_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.groupBox.setTitle(_translate("Eyring_Eq", "Reaction Type"))
        self.unimolecular_radioButton.setText(_translate("Eyring_Eq", "A → P"))
        self.bimolecular_AA_radioButton.setText(_translate("Eyring_Eq", "A + A → P"))
        self.bimolecular_AB_radioButton.setText(_translate("Eyring_Eq", "A + B → P"))
        self.bimolecular_A_Cat_radioButton.setText(_translate("Eyring_Eq", "A + Cat → P + Cat"))
        self.clear_conc2_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.clear_t_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.clear_conv_pushButton.setText(_translate("Eyring_Eq", "×"))
        self.energy_unit_comboBox.setCurrentText(_translate("Eyring_Eq", "kJ/mol"))
        self.energy_unit_comboBox.setItemText(0, _translate("Eyring_Eq", "kJ/mol"))
        self.energy_unit_comboBox.setItemText(1, _translate("Eyring_Eq", "kcal/mol"))
        self.energy_unit_comboBox.setItemText(2, _translate("Eyring_Eq", "eV"))
        self.time_unit_comboBox.setCurrentText(_translate("Eyring_Eq", "s"))
        self.time_unit_comboBox.setItemText(0, _translate("Eyring_Eq", "s"))
        self.time_unit_comboBox.setItemText(1, _translate("Eyring_Eq", "min"))
        self.time_unit_comboBox.setItemText(2, _translate("Eyring_Eq", "h"))
        self.time_unit_comboBox.setItemText(3, _translate("Eyring_Eq", "d"))
        self.time_unit_comboBox.setItemText(4, _translate("Eyring_Eq", "year"))
        self.status_label_2.setText(_translate("Eyring_Eq", "<html><head/><body><p>You can input any Python arithmetic expression, e.g. input 2E3*4.18 for 8360.</p></body></html>"))
        self.status_label_3.setText(_translate("Eyring_Eq", "<html><head/><body><p>If the [Calculate] button is not enabled, check your number of parameters.</p></body></html>"))
        self.status_label_5.setText(_translate("Eyring_Eq", "<html><head/><body><p>Shortcut: Reset - [Ctrl+Shift+R], Calculate - [Ctrl+Shift+C]</p></body></html>"))
