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
		self.filepath = '/Users/Nieo/Library/Logs/Unity/Player.log'
		self.logreader = LogReader(self.filepath)
		self.logreader.logUpdate.connect(self.handleLogUpdate)

		self.updateThread = QThread()
		self.updateThread.started.connect(self.logreader.start)
		self.updateThread.start()
		self.logreader.moveToThread(self.updateThread)		

		self.currentGame = Game()

		self.playerName = 'Nieo'


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


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	a = Control()
	