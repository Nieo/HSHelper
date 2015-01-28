from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from UI.mainWindow import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
	"""docstring for mainW"""
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.decks = QStandardItemModel()
		self.allDecksView.setModel(self.decks)
		
		
	def showDecks(self, decks):
		i = 0
		for d in decks:
			self.decks.setItem(i,0,QStandardItem(d.name))
			i += 1
		self.allDecksView.resize(240, len(decks)*30)
		self.allDecksView.adjustSize()