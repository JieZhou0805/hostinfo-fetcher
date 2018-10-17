# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'float_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(480, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setWindowOpacity(0.8)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(5, 10,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.label_Drag = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_Drag.setFont(font)
        self.label_Drag.setMouseTracking(True)
        self.label_Drag.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Drag.setObjectName("label_Drag")
        self.gridLayout.addWidget(self.label_Drag, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(10, 5,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight
                                          | QtCore.Qt.AlignTrailing
                                          | QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.label_ComputerName = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_ComputerName.setFont(font)
        self.label_ComputerName.setMouseTracking(True)
        self.label_ComputerName.setObjectName("label_ComputerName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label_ComputerName)
        self.label_ComputerName_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_ComputerName_2.setFont(font)
        self.label_ComputerName_2.setMouseTracking(True)
        self.label_ComputerName_2.setText("")
        self.label_ComputerName_2.setAlignment(QtCore.Qt.AlignLeading
                                               | QtCore.Qt.AlignLeft
                                               | QtCore.Qt.AlignVCenter)
        self.label_ComputerName_2.setObjectName("label_ComputerName_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.label_ComputerName_2)
        self.label_CurrentUser = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser.setFont(font)
        self.label_CurrentUser.setMouseTracking(True)
        self.label_CurrentUser.setObjectName("label_CurrentUser")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.label_CurrentUser)
        self.label_CurrentUser_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser_2.setFont(font)
        self.label_CurrentUser_2.setMouseTracking(True)
        self.label_CurrentUser_2.setText("")
        self.label_CurrentUser_2.setAlignment(QtCore.Qt.AlignLeading
                                              | QtCore.Qt.AlignLeft
                                              | QtCore.Qt.AlignVCenter)
        self.label_CurrentUser_2.setObjectName("label_CurrentUser_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.label_CurrentUser_2)
        self.label_CurrentUser_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser_3.setFont(font)
        self.label_CurrentUser_3.setMouseTracking(True)
        self.label_CurrentUser_3.setObjectName("label_CurrentUser_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_CurrentUser_3)
        self.label_CurrentUser_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser_6.setFont(font)
        self.label_CurrentUser_6.setMouseTracking(True)
        self.label_CurrentUser_6.setText("")
        self.label_CurrentUser_6.setObjectName("label_CurrentUser_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.label_CurrentUser_6)
        self.label_CurrentUser_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser_5.setFont(font)
        self.label_CurrentUser_5.setMouseTracking(True)
        self.label_CurrentUser_5.setObjectName("label_CurrentUser_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.label_CurrentUser_5)
        self.label_CurrentUser_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser_7.setFont(font)
        self.label_CurrentUser_7.setMouseTracking(True)
        self.label_CurrentUser_7.setText("")
        self.label_CurrentUser_7.setObjectName("label_CurrentUser_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.label_CurrentUser_7)
        self.label_CurrentUser_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser_4.setFont(font)
        self.label_CurrentUser_4.setMouseTracking(True)
        self.label_CurrentUser_4.setObjectName("label_CurrentUser_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                  self.label_CurrentUser_4)
        self.label_CurrentUser_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_CurrentUser_8.setFont(font)
        self.label_CurrentUser_8.setMouseTracking(True)
        self.label_CurrentUser_8.setText("")
        self.label_CurrentUser_8.setObjectName("label_CurrentUser_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                  self.label_CurrentUser_8)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(10, 5,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_Drag.setText(
            _translate(
                "Form",
                "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Host Information</span></p></body></html>"
            ))
        self.label_ComputerName.setText(
            _translate("Form",
                       "<font color=white><b>Computer Name: </b></font>"))
        self.label_CurrentUser.setText(
            _translate("Form", "<font color=white>Current User: </font>"))
        self.label_CurrentUser_3.setText(
            _translate("Form", "<font color=white>Shared Printer: </font>"))
        self.label_CurrentUser_5.setText(
            _translate("Form", "<font color=white>Network Adapter: </font>"))
        self.label_CurrentUser_4.setText(
            _translate("Form", "<font color=white>IP Address: </font>"))
