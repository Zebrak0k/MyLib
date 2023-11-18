# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/load.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 148)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/icons/ios_share_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(26, 26, 26)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 11, 465, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: rgb(166, 166, 166);\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.load_Button = QtWidgets.QPushButton(self.centralwidget)
        self.load_Button.setGeometry(QtCore.QRect(190, 82, 104, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_Button.sizePolicy().hasHeightForWidth())
        self.load_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.load_Button.setFont(font)
        self.load_Button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.load_Button.setStyleSheet("QPushButton {\n"
"color: rgb(160, 160, 160);\n"
"background-color: rgb(41, 41,41);\n"
"text-align: left;\n"
"border: 2px solid rgb(30, 30, 30);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"text-align: center;\n"
"border-radius: 15px;\n"
"width: 100\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(160, 160, 160);\n"
"background-color: rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(30,30,30);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/resources/icons/download_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_Button.setIcon(icon1)
        self.load_Button.setIconSize(QtCore.QSize(40, 40))
        self.load_Button.setObjectName("load_Button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(430, 110, 31, 28))
        self.exit_button.setStyleSheet("QPushButton {\n"
"color: rgb(160, 160, 160);\n"
"background-color: rgb(41, 41,41);\n"
"text-align: left;\n"
"border: 2px solid rgb(30, 30, 30);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"text-align: center;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(160, 160, 160);\n"
"background-color: rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(30,30,30);\n"
"}")
        self.exit_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/resources/icons/login_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setIconSize(QtCore.QSize(40, 40))
        self.exit_button.setObjectName("exit_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Load"))
        self.label.setText(_translate("MainWindow", "Введите путь к своему pdf файлу"))
        self.load_Button.setText(_translate("MainWindow", "Load"))
import icons_rc