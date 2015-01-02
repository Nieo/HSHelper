import overlay, dbhandler, logreader, time
import tkinter as tk
import threading as th

filepath = '/Users/Nieo/Library/Logs/Unity/Player.log'
#filepath = '/Users/Nieo/Documents/python/Logging/TestLog/Player1.log'
root = tk.Tk() #This should be something usefull instead
ol = overlay.Overlay(root, "opponent plays")
lr = logreader.LogReader(filepath)


def updateGUI():
	global ol
	global lr
	db = dbhandler.DatabaseHandler()
	while True:
		time.sleep(0.01)
		info = lr.getLogEntry()
		if info:
			print(info)
			if "OPPOSING HAND" in info.var1:
				ol.addLabel(info.cardid, db.getCardName(info.cardid))

			if "Hero" in info.var1 and "GRAVEYARD" in info.var2:
				ol.clear()
		


controlthread = th.Thread(target=updateGUI, args=())
controlthread.daemon = True
controlthread.start()
root.mainloop()



