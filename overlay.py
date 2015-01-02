import tkinter as tk

class Overlay(object):
	"""A window that is always on top"""

	def __init__(self, root, labeltext="Overlay"):
		Overlay = tk.Toplevel(root)
		#Overlay.overrideredirect(1)
		#this does not work as it should
		Overlay.wm_attributes("-topmost", 1)
		self.Frame = tk.Frame(Overlay)
		self.Frame.config(bg="black")
		self.Frame.pack()
		self.header = tk.Label(self.Frame, text=labeltext)
		self.header.pack()

		self.labels = {}

	def addLabel(self, cardId, cardName):
		aLabel = None
		try:
			aLabel = self.labels[cardId]
			aLabel.incAmount()
		except KeyError:
			aLabel = LabelFrame(self.Frame,cardName)
			self.labels[cardId] = aLabel
			aLabel.pack()
	
	def clear(self):
		for elem in self.labels:
			self.labels[elem].pack_forget()
			self.labels[elem].destroy()
		self.labels = {}


class LabelFrame(tk.Frame):
	"""Frames for text and values to use in Overlay"""

	def __init__(self, parent,cardName):
		tk.Frame.__init__(self,parent)
		self.config(bd=0, width=100, bg="yellow")
		self.pack()
		self.amount = tk.StringVar()
		self.amount.set(1)
		self.nameLabel = tk.Label(self, text=cardName, bg='red')
		self.amountLabel = tk.Label(self, textvariable=self.amount, bg='teal')
		
		self.nameLabel.pack(side=tk.LEFT)
		self.amountLabel.pack(side=tk.RIGHT)

	def incAmount(self):
		self.amount.set(int(self.amount.get()) + 1)


if __name__ == '__main__':
    root = tk.Tk()
    App = Overlay(root)
    App.addLabel("ID", "NAMe")
    App.addLabel("ID2", "akljfgl")
    App.addLabel("ID2", "Guardian of kings")
    App.addLabel("ID4", "NAMe")
    App.labels['ID'].incAmount()
    root.mainloop()