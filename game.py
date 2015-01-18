import logging
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from Database.dbhandler import DatabaseHandler
class Game(QObject):
	"""Model for a game"""
	

	updateOpponentPlay = pyqtSignal(str) 
	

	def __init__(self):
		super(Game, self).__init__()
		self.database = DatabaseHandler()
		self.opponentPlays = {}

		logging.debug("Created a game")
		

	@pyqtSlot(str)
	def opponentPlay(self, cardid):
		if cardid in self.opponentPlays:
			self.opponentPlays[cardid] += 1
		else:
			self.opponentPlays[cardid] = 1
		self.updateOpponentPlay.emit(self.database.getCardName(cardid))


	def pushOpponentPlay(self):
		for cardid in self.opponentPlays:
			for i in range(0,self.opponentPlays[cardid]):
				self.updateOpponentPlay.emit(self.database.getCardName(cardid))