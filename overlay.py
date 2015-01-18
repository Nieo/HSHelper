
from PyQt5.QtWidgets import QDialog, QLabel, QTableView
from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from UI.overlayDialog import Ui_Dialog

class Overlay(QDialog,Ui_Dialog):
	"""docstring for Overlay"""
	def __init__(self):
		super(Overlay, self).__init__()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.move(10,10)
		self.setupUi(self)
		
		self.values = {}
		self.cards = QStandardItemModel()
		self.tableView.setModel(self.cards)
		self.size = 0


	@QtCore.pyqtSlot(str)
	def addCard(self, name):
		if name not in self.values:
			self.cards.setItem(self.size, 0,QStandardItem(name))
			self.values[name] = QStandardItem('1')
			self.cards.setItem(self.size, 1, self.values[name])
			self.size += 1
			self.tableView.resizeColumnsToContents()
			self.tableView.resize(180,self.tableView.rowHeight(0)* self.size)
			self.adjustSize()
		else:
			self.values[name].setText(str(int(self.values[name].text()) + 1))

	def clear(self):
		self.cards.clear()
		self.size = 0
		self.values = {}
		self.tableView.resize(160, 1)
		self.adjustSize()
