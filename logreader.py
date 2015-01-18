from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, QTimer
import re 

class LogReader(QObject):
	"""docstring for LogReader"""
	logUpdate = pyqtSignal(str, tuple)
	
	def __init__(self, logfile):
		super(QObject, self).__init__()
		self.logfile = open(logfile, 'r')
		self.zoneChange = re.compile(' id=(\d+)[^\[]*cardId=(\w+).*zone from(.*)-> (.*)')

	@pyqtSlot()
	def readLog(self):
		
		self.where = self.logfile.tell()
		line = self.logfile.readline()
		if line:
			zone = self.zoneChange.findall(line)

			if zone != []:
				self.logUpdate.emit('zone', zone[0])
		else:
			self.logfile.seek(self.where)
		

	def start(self):
		print("Called start")
		self.timer = QTimer()
		self.timer.setSingleShot(False)
		self.timer.timeout.connect(self.readLog)
		self.timer.start(0.1)