# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainWindow.ui'
#
# Created: Tue Jan 20 16:46:32 2015
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
        self.cardView = QtWidgets.QListView(self.centralwidget)
        self.cardView.setGeometry(QtCore.QRect(20, 80, 240, 400))
        self.cardView.setObjectName("cardView")
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setGeometry(QtCore.QRect(90, 50, 113, 21))
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(20, 50, 59, 16))
        self.searchLabel.setObjectName("searchLabel")
        self.currentDeckView = QtWidgets.QListView(self.centralwidget)
        self.currentDeckView.setGeometry(QtCore.QRect(280, 80, 240, 400))
        self.currentDeckView.setObjectName("currentDeckView")
        self.currectDeckLabel = QtWidgets.QLabel(self.centralwidget)
        self.currectDeckLabel.setGeometry(QtCore.QRect(280, 50, 111, 16))
        self.currectDeckLabel.setObjectName("currectDeckLabel")
        self.allDecksLabel = QtWidgets.QLabel(self.centralwidget)
        self.allDecksLabel.setGeometry(QtCore.QRect(540, 50, 59, 16))
        self.allDecksLabel.setObjectName("allDecksLabel")
        self.allDecksView = QtWidgets.QListView(self.centralwidget)
        self.allDecksView.setGeometry(QtCore.QRect(540, 80, 240, 400))
        self.allDecksView.setObjectName("allDecksView")
        self.addCardButton = QtWidgets.QPushButton(self.centralwidget)
        self.addCardButton.setGeometry(QtCore.QRect(140, 490, 115, 32))
        self.addCardButton.setObjectName("addCardButton")
        self.removeCardButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeCardButton.setGeometry(QtCore.QRect(280, 490, 141, 32))
        self.removeCardButton.setObjectName("removeCardButton")
        self.newDeckButton = QtWidgets.QPushButton(self.centralwidget)
        self.newDeckButton.setGeometry(QtCore.QRect(540, 490, 115, 32))
        self.newDeckButton.setObjectName("newDeckButton")
        self.removeDeckButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeDeckButton.setGeometry(QtCore.QRect(660, 490, 115, 32))
        self.removeDeckButton.setObjectName("removeDeckButton")
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
        self.searchLabel.setText(_translate("MainWindow", "Search"))
        self.currectDeckLabel.setText(_translate("MainWindow", "Current deck"))
        self.allDecksLabel.setText(_translate("MainWindow", "Decks"))
        self.addCardButton.setText(_translate("MainWindow", "Add to deck"))
        self.removeCardButton.setText(_translate("MainWindow", "Remove from deck"))
        self.newDeckButton.setText(_translate("MainWindow", "New deck"))
        self.removeDeckButton.setText(_translate("MainWindow", "Remove deck"))

