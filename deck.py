
class Deck(object):
	def __init__(self, name, wins=0, losses=0):
		self.name = name
		self.cards = {}