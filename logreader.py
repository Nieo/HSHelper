import threading as th
import re, time 
import queue as qu



class logreader(object):
	"""docstring for LogReader"""
	def __init__(self, location):
		super(logreader, self).__init__()
		self.file = open(location, 'r')
		self.action = re.compile(' id=(\d+)[^\[]*cardId=(\w+).*zone from(.*)->(.*)')
		self.queue = qu.Queue()
		self.keepreading = True
		self.readthread = th.Thread(target=self.readlog, args=())
		self.readthread.daemon = True
		self.readthread.start()

	def getlogentry(self):
		print("getaction")
		entry = None
		try: 
			with th.Lock():
				entry = self.queue.get(block=False)
		except qu.Empty:
			pass
		return entry

	def stopreading(self):
		self.keepreading = False

	def readlog(self):
		
		while self.keepreading:
			self.where = self.file.tell()
			line = self.file.readline()
			if not line:
				time.sleep(0.01)
				self.file.seek(self.where)
			else:
				anything = self.action.findall(line)
				#print(anything)
				if anything != []:
					with th.Lock():
						self.queue.put(logentry(anything[0][0], anything[0][1], anything[0][2], anything[0][3]), block=False)


class logentry(object):
	"""docstring for logentry"""
	def __init__(self, entityid, cardid, var1=None, var2=None):
		super(logentry, self).__init__()	
		self.entityid = entityid
		self.cardid = cardid
		self.var1 = var1
		self.var2 = var2

	def __str__(self):
		return "entityid={0}, cardid={1}, var1={2}, var2={3}".format(self.entityid, self.cardid, self.var1, self.var2)
	
	def getentityid():
		return self.entityid

	def getcardid():
		return self.cardid

	def getvar1():
		return self.var1

	def getvar2():
		return self.var2


if __name__ == '__main__':
	lr = logreader('/Users/Nieo/Documents/python/Logging/TestLog/Player1.log')
	print("Started")
	time.sleep(1)
	print(lr.getlogentry())
	lr.stopreading()
	print(lr.getlogentry())







