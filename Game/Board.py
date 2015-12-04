
from Game.Deck import Deck
from Game.Card import Card
from Game.Hand import Hand

class Board():
    def __init__(self, deck, heroClass):
        initGame(deck)
       
    def initGame(self, deck):
        #Your data
        self.hand = Hand()
        self.deck = deck
        self.myMinions = []
        self.myHealth = 30
        self.myArmor = 0
        #Enemy data
        self.enemyHandSize = 0
        self.enemyDeckSize = 30
        self.enemyMinions = []
        self.enemyHealth = 30
        self.enemyArmor = 0

    def drawCard(self, cardid):
        self.hand.addCard(self.deck.drawCard(cardid))

    def enemyDrawCard(self):
        self.enemyHandSize += 1
        self.enemyDeckSize -= 1

