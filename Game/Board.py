
from Game.Deck import Deck
from Game.Card import Card
from Game.Hand import Hand

class Board():
    def __init__(self, deck, heroClass):
        self.initGame(deck)

    def initGame(self, deck):
        #Your data
        self.hand = Hand()
        self.deck = deck
        self.deckSize = 0
        self.myMinions = []
        self.myHealth = 30
        self.myArmor = 0
        #Enemy data
        self.enemyHandSize = 0
        self.enemyDeckSize = 0
        self.enemyMinions = []
        self.enemyHealth = 30
        self.enemyArmor = 0

    def mulligan(self, id):
        self.hand.getCard(id)
        self.deckSize += 1

    def drawCard(self, id, cardid):
        self.deckSize -= 1
        self.deck.drawCard(cardid)
        self.hand.addCard(id, cardid)

    def enemyDrawCard(self):
        self.enemyHandSize += 1
        self.enemyDeckSize -= 1

    def enemyPlayCard(self, cardid):
        self.enemyHandSize -= 1

    def castSpell(self, id):
        self.hand.getCard(id)

    def playMinion(self, id):
        minion = self.hand.getCard(id)

    def __str__(self):
        state = """Current state
        My health/armor {0.myHealth}/{0.myArmor}\tEnemy health/armor {0.enemyHealth}/{0.enemyArmor}
        My hand/deck size {1}/{0.deckSize}\tEnemy hand/deck size {0.enemyHandSize}/{0.enemyDeckSize}
            """.format(self, self.hand.size())
        return state

