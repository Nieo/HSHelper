import sqlite3, logging

class DatabaseHandler():
	"""Handles the hearthstone database"""
	def __init__(self):
		super(DatabaseHandler, self).__init__()
		logging.debug("DatabaseHandler trying to connect to database")
		try:
			self.db = sqlite3.connect('Database/Hearthstone.db')
			self.cursor = self.db.cursor()
			logging.info("DatabaseHandler is connected")
		except sqlite3.Error as err:
			logging.warning("sqlite3.Error : {0}".format(err))

	def runQuery(self, query):
		logging.debug("Running query: " + query)
		try:
			self.cursor.execute(query)
			self.db.commit()
		except sqlite3.Error as err:
			logging.warning("sqlite3.Error : {0}".format(err))

	def getCardName(self, cardId):
		logging.debug("called DatabaseHandler.getCardName")
		try:
			query = "SELECT name FROM cards WHERE id=\'" + cardId + "\';"
			self.cursor.execute(query)

			name = self.cursor.fetchone()
			if name:
				return name[0]
		except sqlite3.Error as err:
			logging.warning("sqlite3.Error : {0}".format(err))

	def addDeck(self, name):
		logging.debug("called DatabaseHandler.addDeck")
		query = "INSERT INTO decks (name) VALUES('"+ name +"');"
		self.runQuery(query)

	def getDecks(self):
		logging.debug("called DatabaseHandler.getDecks")
		query = "SELECT rowid, * FROM decks;"
		self.runQuery(query)
		return self.cursor.fetchall()

	def changeDeckName(self, oldName, newName):
		logging.debug("called DatabaseHandler.changeDeckName from {0} to {1}".format(oldName, newName))
		query = "UPDATE decks SET name='{0}' WHERE name='{1}'".format(oldName, newName)
		self.runQuery(query)


	def addCardToDeck(self, cardid, deckid, numberof):
		logging.debug("called DatabaseHandler.addCardToDeck with {0},{1},{2}".format(cardid,deckid,numberof))
		query = "SELECT * FROM cardsInDeck WHERE cardid='{0}' AND deckid={1} AND numberof={2};".format(cardid,deckid,numberof)
		self.runQuery(query)
		exist = self.cursor.fetchone()
		if not exist:
			query = "INSERT INTO cardsInDeck VALUES ('{0}',{1},{2},0,0,0)".format(cardid,deckid,numberof)
		else:
			query = "UPDATE cardsInDeck SET indeck=1 WHERE cardid='{0}' AND deckid={1} AND numberof={2};".format(cardid,deckid,numberof)
		self.runQuery(query)

	def removeCardFromDeck(self, cardid, deckid, numberof):
		logging.debug("called DatabaseHandler.removeCardFromDeck with {0},{1},{2}".format(cardid,deckid,numberof))
		query = "UPDATE cardsInDeck SET indeck=0 WHERE cardid='{0}' AND deckid={1} AND numberof={2};".format(cardid,deckid,numberof)
		self.runQuery(query)

	def findCards(self, searchTerm):
		logging.debug("called DatabaseHandler.getCardByCost with " + searchTerm)
		query = "SELECT id, name FROM cards WHERE (name LIKE '%{0}%' OR cost='{0}' )AND (type='Minion' OR type='Spell');".format(searchTerm)
		self.runQuery(query)
		return self.cursor.fetchall()


	def shutdown(self):
		logging.debug("called DatabaseHandler.shutdown")
		self.db.close()


