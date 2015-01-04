import overlay, dbhandler, logreader, window, time
import tkinter as tk
import threading as th



class control(object):
	"""docstring for control"""


	def __init__(self):
		super(control, self).__init__()
		
		self.filepath = '/Users/Nieo/Library/Logs/Unity/Player.log'

		self.db = dbhandler.DatabaseHandler()
		self.lr = logreader.LogReader(self.filepath)
		self.root = window.Window(self.windowCommand)
		self.ol = overlay.Overlay(self.root, "opponent plays")


		self.root.after(100,self.updateGUI)
		self.root.mainloop()

	def windowCommand(self,command, data=None):
		print(command + " : " + str(data))
		if "clear" in command:
			self.ol.clear()
		if "adddeck" in command:
			self.db.addDeck(data)

	def updateGUI(self):
		db = dbhandler.DatabaseHandler()
		info = self.lr.getLogEntry()
		#print(info)
		if info:
			if "OPPOSING HAND" in info.var1:
				self.ol.addLabel(info.cardid, db.getCardName(info.cardid))

			if "Hero" in info.var1 and "GRAVEYARD" in info.var2:
				self.ol.clear()
		self.root.after(10,self.updateGUI)



if __name__ == '__main__':
	a = control()


