class Deck(object):
	"""docstring for Deck"""
	def __init__(self, deckid, name, wins=0, losses=0):
		super(Deck, self).__init__()
		self.deckid = deckid
		self.name = name
		self.wins = wins
		self.losses = losses
		self.cards = {}

	def __str__(self):
		return "Deckid: " + str(self.deckid) + ", name: " + self.name
