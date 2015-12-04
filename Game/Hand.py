class Hand(object):
    """docstring for Hand"""
    def __init__(self, arg):
        self.cards = []
        self.maxMana = 0
        self.currentMana = 0


    def addCard(self, card):
        self.cards.append(card)


