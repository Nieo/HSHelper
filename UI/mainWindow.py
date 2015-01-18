# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainWindow.ui'
#
# Created: Sun Jan 11 08:09:19 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnemyDrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnemyDrawButton.setGeometry(QtCore.QRect(0, 0, 141, 32))
        self.EnemyDrawButton.setObjectName("EnemyDrawButton")
        self.ClearEnemyButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearEnemyButton.setGeometry(QtCore.QRect(130, 0, 115, 32))
        self.ClearEnemyButton.setObjectName("ClearEnemyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EnemyDrawButton.setText(_translate("MainWindow", "Show enemy draw"))
        self.ClearEnemyButton.setText(_translate("MainWindow", "Clear"))

