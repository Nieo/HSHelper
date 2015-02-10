import sys, logging
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from game import Game
from mainwindow import MainWindow
from overlay import Overlay
from logreader import LogReader
from Database.dbhandler import DatabaseHandler
from deck import Deck
class Control(QObject):
	"""Main controler"""


	def __init__(self):
		super(Control, self).__init__()
		self.app = QApplication(sys.argv)
		#Mainwindow
		self.mainWindow = MainWindow()
		self.mainWindow.show()
		self.mainWindow.deckSelectedSignal.connect(self.deckSelected)
		self.mainWindow.newDeckSignal.connect(self.newDeck)
		self.mainWindow.deckNameChangedSignal.connect(self.deckNameChanged)
		self.mainWindow.searchLineEdit.textChanged.connect(self.searchForCards)
		#Logreader
		self.filepath = '/Users/Nieo/Library/Logs/Unity/Player.log'
		self.logreader = LogReader(self.filepath)
		self.logreader.logUpdate.connect(self.handleLogUpdate)
		self.updateThread = QThread()
		self.updateThread.started.connect(self.logreader.start)
		self.updateThread.start()
		self.logreader.moveToThread(self.updateThread)


		#DB
		self.database = DatabaseHandler()

		self.selectedDeck = None
		self.decks = []
		tmp = self.database.getDecks()
		for i in tmp:
			self.decks.append(Deck(i[0],i[1],i[2]))

		self.currentGame = Game()

		self.playerName = 'Nieo'

		self.mainWindow.showDecks(self.decks)

		self.overlay = Overlay()
		self.overlay.show()

		sys.exit(self.app.exec_())


	@pyqtSlot(str, tuple)
	def handleLogUpdate(self, type, data):
		if type == "zone":
			if data[2] == "OPPOSING HAND":
				self.currentGame.opponentPlay(data[1])
			else:
				pass
				#logging.debug(data)
		elif type == "playState":
			logging.debug(data)
			if data[1] == 'PLAYING' and data[0] == self.playerName:
				logging.info("New game starting")
				self.overlay.clear()
				self.currentGame = Game()
				self.currentGame.updateOpponentPlay.connect(self.overlay.addCard)

			elif data[1] == 'WON':
				if data[0] == self.playerName:
					logging.info("You have won")
				else:
					logging.info("You have lost")
	@pyqtSlot()
	def newDeck(self):
		logging.debug("New deck created")
		self.database.addDeck('New Deck')

	@pyqtSlot(str)
	def deckNameChanged(self, name):
		self.database.changeDeckName(name, self.selectedDeck)

	@pyqtSlot(str)
	def deckSelected(self, deckname):
		self.selectedDeck = deckname
		logging.debug("deckSelected: " + self.selectedDeck)

	@pyqtSlot(str)
	def searchForCards(self, query):
		if(query):
			cards = self.database.findCards(query)
			self.mainWindow.showFoundCards(cards)

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	a = Control()



