from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from UI.mainWindow import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
	"""docstring for mainW"""
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)

        self.decks = QStandardItemModel()

