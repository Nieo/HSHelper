
class Board():
    def __init__(self, deck, class):
#You data
        self.hand = Hand()
        self.deck = Deck()
        self.myMinions = []
        self.myHealth = 30
        self.myArmor = 0


#Enemy data
        self.enemyHandSize = 0
        self.enemyDeckSize = 0
        self.enemyMinions = []
        self.enemyHealth = 30
        self.enemyArmor = 0


    def drawCard(self, cardid):
        self.hand.addCard(self.deck.drawCard(cardid))

    def enemyDrawCard(self):
        self.enemyHandSize += 1
        self.enemyDeckSize -= 1

