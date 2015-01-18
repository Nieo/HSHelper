import sys, logging 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from game import Game
from mainwindow import MainWindow
from overlay import Overlay
from logreader import LogReader
from Database.dbhandler import DatabaseHandler
class Control(QObject):
	"""Main controler"""
	
	


	def __init__(self):
		super(Control, self).__init__()
		self.app = QApplication(sys.argv)
		self.mainWindow = MainWindow(self.callback)
		self.mainWindow.show()
		self.filepath = 'Player.log'#/Users/Nieo/Library/Logs/Unity/Player.log'
		self.logreader = LogReader(self.filepath)
		self.logreader.logUpdate.connect(self.handleLogUpdate)

		self.updateThread = QThread()
		self.updateThread.started.connect(self.logreader.start)
		self.updateThread.start()
		self.logreader.moveToThread(self.updateThread)		

		self.currentGame = Game()

		self.foundHeroes = 0

		self.overlay = Overlay()
		self.overlay.show()

		sys.exit(self.app.exec_())
		

	def callback(self, data):
		if data == 'displayEnemyDraw':
			pass
	
		if data == "test":
			pass
	
	@pyqtSlot(str, tuple)
	def handleLogUpdate(self, type, data):
		if type == "zone":
			if "Hero" in data[2]:
				logging.debug(data)
				logging.info("Game over")
			elif "(Hero)" in data[3]:
				if self.foundHeroes == 1:
					logging.info("New game starting")
					self.overlay.clear()
					self.currentGame = Game()
					self.currentGame.updateOpponentPlay.connect(self.overlay.addCard)

				self.foundHeroes = (1+self.foundHeroes)%2
			
				
			elif data[3] == "OPPOSING PLAY":
				self.currentGame.opponentPlay(data[1]) 


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	a = Control()
	