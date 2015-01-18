from PyQt5.QtWidgets import QMainWindow
from UI.mainWindow import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
	"""docstring for mainW"""
	def __init__(self, callback):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.callback = callback

		self.EnemyDrawButton.clicked.connect(self.displayEnemyDraw)
		self.ClearEnemyButton.clicked.connect(self.test)
	def displayEnemyDraw(self):
		self.callback("displayEnemyDraw")

	def clearEnemyDraw(self):
		self.callback("clearEnemyDraw")

	def test(self):
		self.callback("test")