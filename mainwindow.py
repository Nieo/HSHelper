from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from UI.mainWindow import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
	"""docstring for mainW"""

	newDeckSignal = pyqtSignal()
	deckSelectedSignal = pyqtSignal(str)
	deckNameChangedSignal = pyqtSignal(str)

	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.decks = QStandardItemModel()
		self.allDecksView.setModel(self.decks)
		self.allDecksView.clicked.connect(self.deckViewClicked)
		self.newDeckButton.clicked.connect(self.newDeck)
		self.decks.itemChanged.connect(self.deckNameChanged)

	def showDecks(self, decks):
		for d in decks:
			item = QStandardItem(d.name)
			self.decks.appendRow(item)

	def deckViewClicked(self):
		if self.allDecksView.selectionModel().selectedRows()[0]:
			self.deckSelectedSignal.emit(self.decks.item(self.allDecksView.selectionModel().selectedRows()[0].row()).text())

	def newDeck(self):
		item = QStandardItem("New Deck")
		self.decks.appendRow(item)
		self.allDecksView.edit(self.decks.indexFromItem(item))
		self.newDeckSignal.emit()
		self.deckSelectedSignal.emit("New Deck")


	def deckNameChanged(self):
		self.deckNameChangedSignal.emit(self.decks.item(self.allDecksView.selectionModel().selectedRows()[0].row()).text())

