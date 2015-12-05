class Hand(object):
    """docstring for Hand"""
    def __init__(self):
        self.cards = {}
        self.maxMana = 0
        self.currentMana = 0


    def addCard(self, id, card):
        self.cards[id] = card

    def getCard(self, id):
        card = self.cards[id]
        del self.cards[id]
        return card

    def size(self):
        return len(self.cards)
