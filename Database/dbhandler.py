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
		try: 
			query = "INSERT INTO decks (name, wins, losses)VALUES('{0}',0,0);".format(name)
			self.cursor.execute(query)
			self.db.commit()
		except sqlite3.Error as err:
			logging.warning("sqlite3.Error : {0}".format(err))
	
	def getDecks(self):
		logging.debug("called DatabaseHandler.getDecks")
		try:
			query = "SELECT * FROM decks;"
			self.cursor.execute(query)
			self.db.commit()
			return self.cursor.fetchall()
		except sqlite3.Error as err:
			logging.warning("sqlite3.Error : {0]".format(err))

	def getDeckData(self, id):
		logging.debug("called DatabaseHandler.getDeckData")
		try:
			query = "SELECT name,wins,losses FROM decks WHERE id={0};".format(id)
			self.cursor.execute(query)
			self.db.commit()
			data = self.cursor.fetchone()
			return data
		except sqlite3.Error as err:
			logging.warning("sqlite3.Error : {0}".format(err))

	def updateDeckData(self, id, win):
		logging.debug("called DatabaseHandler.updateDeckData")
		currentStats = self.getDeckData(id)
		if win:
			toUpdate = 'wins'
			newValue = currentStats[1] + 1
		else: 
			toUpdate = 'losses'
			newValue = currentStats[2] + 1
		try:
			query = "UPDATE decks SET '{0}'={1} WHERE id={2};".format(toUpdate,newValue,id)
			self.cursor.execute(query)
			self.db.commit()			
		except sqlite3.Error as err:
			logging.warning("sqlite3.Error : {0}".format(err))

	def shutdown(self):
		logging.debug("called DatabaseHandler.shutdown")
		self.db.close()

if __name__ == '__main__':
	db = DatabaseHandler()
	db.addDeck("TestDeck")
	data = db.getDeckData(1)
	print(data)
	db.updateDeckData(1,False)
	data = db.getDeckData(1)
	print(data)
	print(db.getCardName("GAME_005"))
	db.shutdown()