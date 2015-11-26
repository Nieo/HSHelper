from PyQt5.QtCore import pyqtSignal, QItemSelectionModel
from PyQt5.QtSql import QSqlRelationalTableModel
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
        # SearchCards
        self.foundCards = QStandardItemModel()
        self.cardView.setModel(self.foundCards)
        # CardsInDeck
        self.selectedDeck = QSqlRelationalTableModel()
        # sself.selectedDeck.setTable()
        self.currentDeckView.setModel(self.selectedDeck)
        # Decks
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
            self.deckSelectedSignal.emit(self.decks.item(
                self.allDecksView.selectionModel().selectedRows()[0].row()).text())

    def newDeck(self):
        self.allDecksView.selectionModel().reset()
        item = QStandardItem("New Deck")
        self.decks.appendRow(item)
        index = self.decks.indexFromItem(item)
        self.allDecksView.edit(index)
        self.allDecksView.selectionModel().select(
            index, QItemSelectionModel.Select)
        self.newDeckSignal.emit()
        self.deckSelectedSignal.emit("New Deck")

    def deckNameChanged(self):
        self.deckNameChangedSignal.emit(self.decks.item(
            self.allDecksView.selectionModel().selectedRows()[0].row()).text())

    def showFoundCards(self, cards):
        self.foundCards.clear()
        for c in cards:
            card = QStandardItem(c[1])
            self.foundCards.appendRow(card)
