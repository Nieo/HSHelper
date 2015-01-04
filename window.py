import tkinter as tk
import dbhandler
class Window(tk.Frame):
	"""Main window"""

	def __init__(self, callback):
		tk.Frame.__init__(self,master=None)
		self.callback = callback
		self.db = dbhandler.DatabaseHandler()
		self.grid()
		self.nameLabel = tk.Label(self, text="Deckname")
		self.nameLabel.grid(row=0,column=0)
		self.nameEntry = tk.Entry(self, width=10)
		self.nameEntry.grid(row=0,column=1)
		self.createDeckButton = tk.Button(self, text="Create Deck", command=self.addDeck)
		self.createDeckButton.grid(row=0,column=2)
		self.clearButton = tk.Button(self, text="Clear", command=self.clearOverlay)
		self.clearButton.grid(row=1, column=0)
		self.statFrame = deckStatsFrame(self, "DeckName", "G", "W","L","%")
		self.statFrame.grid(columnspan = 4, row=2, column=0)
		self.statFrames = {}
		self.addDeckStatsFrames()

	def clearOverlay(self):
		self.callback("clear")

	def addDeck(self): 
		self.callback("adddeck", self.nameEntry.get())

	def addDeckStatsFrames(self):
		deckdata = self.db.getDecks()
		i = 3
		for item in deckdata:
			games = item[2]+item[3]
			winrate = None
			if games:
				winrate = item[2]/games
			self.statFrames[item[0]] = deckStatsFrame(self, item[1], games, item[2], item[3], winrate)
			self.statFrames[item[0]].grid(columnspan = 4, row=i, column=0)
			i += 1

class deckStatsFrame(tk.Frame):
	"""docstring for deckStatsFrame"""
	def __init__(self,parent, name, games, wins, losses, winrate):
		tk.Frame.__init__(self, parent)
		self.w = 3
		self.grid()
		self.nameLabel = tk.Label(self, text=name, width=10)
		self.nameLabel.grid(row=0,column=0)
		self.gameLabel = tk.Label(self, text=games ,width=self.w)
		self.gameLabel.grid(row=0,column=1)
		self.winsLabel = tk.Label(self, text=wins, width=self.w)
		self.winsLabel.grid(row=0,column=2)
		self.lossesLabel = tk.Label(self, text=losses, width=self.w)
		self.lossesLabel.grid(row=0,column=3)
		self.winrateLabel = tk.Label(self, text=winrate, width=self.w)
		self.winrateLabel.grid(row=0,column=4)
