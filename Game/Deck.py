class Deck(object):
    """docstring for Deck"""
    def __init__(self, cards):
        self.cards = []

    def drawCard(self, cardid):
        self.cards.remove(cardid)
