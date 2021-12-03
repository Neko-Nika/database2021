# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\connectWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnectWindow(object):
    def setupUi(self, ConnectWindow):
        ConnectWindow.setObjectName("ConnectWindow")
        ConnectWindow.resize(400, 550)
        ConnectWindow.setMinimumSize(QtCore.QSize(400, 550))
        ConnectWindow.setMaximumSize(QtCore.QSize(400, 550))
        self.centralwidget = QtWidgets.QWidget(ConnectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 401, 551))
        self.widget.setStyleSheet("border-radius:10px;")
        self.widget.setObjectName("widget")
        self.userText = QtWidgets.QLineEdit(self.widget)
        self.userText.setGeometry(QtCore.QRect(75, 60, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userText.setFont(font)
        self.userText.setAlignment(QtCore.Qt.AlignCenter)
        self.userText.setObjectName("userText")
        self.connectButton = QtWidgets.QPushButton(self.widget)
        self.connectButton.setGeometry(QtCore.QRect(75, 430, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.connectButton.setFont(font)
        self.connectButton.setStyleSheet("QPushButton#connectButton{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton#connectButton:pressed{\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"background-color:rgba(0, 0, 0, 100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#connectButton{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"}")
        self.connectButton.setObjectName("connectButton")
        self.passwordText = QtWidgets.QLineEdit(self.widget)
        self.passwordText.setGeometry(QtCore.QRect(75, 150, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordText.setFont(font)
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordText.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordText.setObjectName("passwordText")
        self.databaseText = QtWidgets.QLineEdit(self.widget)
        self.databaseText.setGeometry(QtCore.QRect(75, 240, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.databaseText.setFont(font)
        self.databaseText.setAlignment(QtCore.Qt.AlignCenter)
        self.databaseText.setObjectName("databaseText")
        self.hostText = QtWidgets.QLineEdit(self.widget)
        self.hostText.setGeometry(QtCore.QRect(75, 330, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hostText.setFont(font)
        self.hostText.setAlignment(QtCore.Qt.AlignCenter)
        self.hostText.setObjectName("hostText")
        ConnectWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ConnectWindow)
        self.statusbar.setObjectName("statusbar")
        ConnectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConnectWindow)
        QtCore.QMetaObject.connectSlotsByName(ConnectWindow)

    def retranslateUi(self, ConnectWindow):
        _translate = QtCore.QCoreApplication.translate
        ConnectWindow.setWindowTitle(_translate("ConnectWindow", "MainWindow"))
        self.userText.setPlaceholderText(_translate("ConnectWindow", "Пользователь"))
        self.connectButton.setText(_translate("ConnectWindow", "П О Д К Л Ю Ч И Т Ь С Я"))
        self.passwordText.setPlaceholderText(_translate("ConnectWindow", "Пароль"))
        self.databaseText.setPlaceholderText(_translate("ConnectWindow", "Имя базы данных"))
        self.hostText.setPlaceholderText(_translate("ConnectWindow", "Хост"))