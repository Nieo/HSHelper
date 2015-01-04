import threading as th
import re, time 
import queue as qu



class LogReader(object):
	"""docstring for LogReader"""
	def __init__(self, location):
		super(LogReader, self).__init__()
		self.file = open(location, 'r')
		self.action = re.compile(' id=(\d+)[^\[]*cardId=(\w+).*zone from(.*)->(.*)')
		self.queue = qu.Queue()
		self.keepreading = True
		self.readthread = th.Thread(target=self.readLog, args=())
		self.readthread.daemon = True
		self.readthread.start()

	def getLogEntry(self):
		entry = None
		try: 
			with th.Lock():
				entry = self.queue.get(block=False)
		except qu.Empty:
			pass
		return entry

	def stopReading(self):
		self.keepreading = False

	def readLog(self):
		
		while True:
			self.where = self.file.tell()
			line = self.file.readline()
			if not line:
				time.sleep(0.1)
				self.file.seek(self.where)
			else:
				anything = self.action.findall(line)
				if anything != []:
					with th.Lock():
						self.queue.put(LogEntry(anything[0][0], anything[0][1], anything[0][2], anything[0][3]), block=False)

class LogEntry(object):
	"""docstring for logentry"""
	def __init__(self, entityid, cardid, var1=None, var2=None):
		super(LogEntry, self).__init__()	
		self.entityid = entityid
		self.cardid = cardid
		self.var1 = var1
		self.var2 = var2

	def __str__(self):
		return "entityid={0}, cardid={1}, var1={2}, var2={3}".format(self.entityid, self.cardid, self.var1, self.var2)


if __name__ == '__main__':
	lr = LogReader('/Users/Nieo/Documents/python/Logging/TestLog/Player1.log')
	print("Started")
	time.sleep(1)
	print(lr.getLogEntry())
	
	print(lr.getLogEntry())
	time.sleep(10)






