#Creates/recreate database and adds all cards and initiates a database for decks 
#THIS MAY DESTROY DATA
import sqlite3 as lite
import json

def createDatabase(databasename, cardset):

	cardfile = open(cardset)
	cards = json.loads(cardfile.read())

	try:
		db = lite.connect(databasename)
		cursor = db.cursor()
		cursor.execute("DROP TABLE IF EXISTS cards;")
		createcardsquery = """CREATE TABLE cards(
			name TEXT,
			cost INT,
			type TEXT,
			rarity TEXT,
			faction TEXT,
			race TEXT,
			playerClass TEXT,
			text TEXT,
			inPlayText TEXT,
			mechanics TEXT,
			flavor TEXT,
			artist TEXT,
			attack INT,
			health INT,
			duability INT,
			id TEXT,
			collectible TEXT,
			elite TEXT,
			howToGet TEXT,
			howToGetGold TEXT
			);"""

		print("Executing: " + createcardsquery)
		cursor.execute(createcardsquery)
		
		for set in cards:
			for card in cards[set]:
				cardquery = """INSERT INTO cards VALUES(
					'{0}',
					{1},
					'{2}',
					'{3}',
					'{4}',
					'{5}',
					'{6}',
					'{7}',
					'{8}',
					'{9}',
					'{10}',
					'{11}',
					{12},
					{13},
					{14},
					'{15}',
					'{16}',
					'{17}',
					'{18}',
					'{19}'
					);""".format(
					card.get('name').replace('\'', '\'\''),
					card.get('cost') if type(card.get('cost')) is int else 'NULL',
					card.get('type'),
					card.get('rarity'), 
					card.get('faction'),
					card.get('race'),
					card.get('playerClass'),
					card.get('text').replace('\'', '\'\'') if type(card.get('text')) is str else None,
					card.get('inPlayText').replace('\'', '\'\'') if type(card.get('inPlayText')) is str else None,
					str(card.get('mechanics')).replace('\'', '\'\'') if type(card.get('mechanics')) is list else None,
					card.get('flavor').replace('\'', '\'\'') if type(card.get('flavor')) is str else None,
					card.get('artist').replace('\'', '\'\'') if type(card.get('artist')) is str else None,
					card.get('attack') if type(card.get('attack')) is int else 'NULL',
					card.get('health') if type(card.get('health')) is int else 'NULL',
					card.get('duability') if type(card.get('duability')) is int else 'NULL',
					card.get('id'),
					card.get('collectible'),
					card.get('elite'),
					card.get('howToGet').replace('\'', '\'\'') if type(card.get('howToGet')) is str else None,
					card.get('howToGetGold').replace('\'', '\'\'') if type(card.get('howToGetGold')) is str else None
					)
				
				#print("Executing: " + cardquery)
				cursor.execute(cardquery)
				db.commit()
		
		cursor.execute("DROP TABLE IF EXISTS decks")
		createdecksquery = """CREATE TABLE decks(
			id INTEGER PRIMARY KEY,
			name TEXT,
			wins INT NOT NULL,
			losses INT NOT NULL
			);"""		
		print("Executing: " + createdecksquery)
		cursor.execute(createdecksquery)

		db.commit


	except lite.Error as err:
		print("sqlite3.Error " + str(err))
	finally:
		if db:
			print('No errors ')
			db.close()


if __name__ == '__main__':
	dbname = "Hearthstone.db"
	jsonfile = "AllSets.enUS.json"	
	createDatabase(dbname,jsonfile)

