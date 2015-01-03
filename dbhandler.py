import sqlite3

class DatabaseHandler():
	"""Handles the hearthstone database"""
	def __init__(self):
		super(DatabaseHandler, self).__init__()
		try:
			self.db = sqlite3.connect('Hearthstone.db')
			self.cursor = self.db.cursor()
		except sqlite3.Error as err:
			print("sqlite3.Error : {0}".format(err))

	def getCardName(self, cardId):
		try:
			query = "SELECT name FROM cards WHERE id=\'" + cardId + "\';"
			self.cursor.execute(query)
			
			name = self.cursor.fetchone()
			if name:
				return name[0]
		except sqlite3.Error as err:
			print("sqlite3.Error : {0}".format(err))

	def addDeck(self, name):
		try: 
			query = "INSERT INTO decks (name, wins, losses)VALUES('{0}',0,0);".format(name)
			self.cursor.execute(query)
			self.db.commit()
		except sqlite3.Error as err:
			print("sqlite3.Error : {0}".format(err))
	
	def getDecks(self):
		try:
			query = "SELECT * FROM decks;"
			self.cursor.execute(query)
			self.db.commit()
			return self.cursor.fetchall()
		except sqlite3.Error as err:
			print("sqlite3.Error : {0]".format(err))

	def getDeckData(self, id):
		try:
			query = "SELECT name,wins,losses FROM decks WHERE id={0};".format(id)
			self.cursor.execute(query)
			self.db.commit()
			data = self.cursor.fetchone()
			return data
		except sqlite3.Error as err:
			print("sqlite3.Error : {0}".format(err))

	def updateDeckData(self, id, win):
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
			print("sqlite3.Error : {0}".format(err))

	def shutdown(self):
		self.db.close()

if __name__ == '__main__':
	db = DatabaseHandler()
	db.addDeck("TestDeck", "Not A hero")
	data = db.getDeckData(1)
	print(data)
	db.updateDeckData(1,False)
	data = db.getDeckData(1)
	print(data)
	print(db.getCardName("GAME_005"))
	db.shutdown()