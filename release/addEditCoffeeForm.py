# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow_1):
        MainWindow_1.setObjectName("MainWindow_1")
        MainWindow_1.resize(723, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow_1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 50, 81, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 80, 281, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 80, 251, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 110, 311, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 110, 251, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 200, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 260, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 320, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 370, 113, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(300, 410, 411, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(300, 500, 113, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(300, 550, 113, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 600, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 180, 139, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        MainWindow_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_1)
        self.statusbar.setObjectName("statusbar")
        MainWindow_1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_1)

    def retranslateUi(self, MainWindow_1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_1.setWindowTitle(_translate("MainWindow_1", "MainWindow"))
        self.label.setText(_translate("MainWindow_1", "Изменение(все поля обязательны к заполнению):"))
        self.label_2.setText(_translate("MainWindow_1", "ID(номер записи, которую хотите изменить)"))
        self.label_3.setText(_translate("MainWindow_1", "Названия столбцов, которые хотите изменить"))
        self.label_4.setText(_translate("MainWindow_1", "Изменения(в порядке названий столбцов, через ;)"))
        self.label_5.setText(_translate("MainWindow_1", "Добавление(все поля обязательны к заполнению):"))
        self.pushButton.setText(_translate("MainWindow_1", "ОК"))
        self.label_12.setText(_translate("MainWindow_1", "ID"))
        self.label_9.setText(_translate("MainWindow_1", "Название сорта"))
        self.label_11.setText(_translate("MainWindow_1", "Степень обжарки"))
        self.label_10.setText(_translate("MainWindow_1", "Молотый/в зёрнах"))
        self.label_8.setText(_translate("MainWindow_1", "Вкус"))
        self.label_6.setText(_translate("MainWindow_1", "Цена(за вес; в рублях)"))
        self.label_7.setText(_translate("MainWindow_1", "Вес(в граммах)"))
