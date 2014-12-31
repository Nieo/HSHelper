import sqlite3

class DatabaseHandler():
	"""Handles the hearthstone database"""
	def __init__(self):
		super(DatabaseHandler, self).__init__()
		try:
			self.db = sqlite3.connect('Data/Heartstone')
			self.cursor = self.db.cursor()
		except sqlite3.Error as err:
			print("sqlite3.Error : {0}".format(err))

	def addDeck(self, name, hero):
		try: 
			query = "INSERT INTO Decks (name, class, wins, losses)VALUES('{0}','{1}',0,0);".format(name,hero)
			self.cursor.execute(query)
			self.db.commit()
		except sqlite3.Error as err:
			print("sqlite3.Error : {0}".format(err))
	
	def getDeckData(self, id):
		try:
			query = "SELECT name,wins,losses FROM Decks WHERE id={0};".format(id)
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
			query = "UPDATE Decks SET '{0}'={1} WHERE id={2};".format(toUpdate,newValue,id)
			self.cursor.execute(query)
			self.db.commit()			
		except sqlite3.Error as err:
			print("sqlite3.Error : {0}".format(err))

	def shutdown(self):
		self.db.close()

if __name__ == '__main__':
	db = DatabaseHandler()
	data = db.getDeckData(1)
	print(data)
	db.updateDeckData(1,False)
	data = db.getDeckData(1)
	print(data)
	db.shutdown()