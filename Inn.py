#!/usr/bin/python
from Game.Board import Board
from logreader import LogReader
from Game.Deck import Deck
from Database import dbhandler

class Inn(object):
    def __init__(self):
        self.filepath = '/Users/Nieo/Library/Logs/Unity/Player.log'
        self.logreader = LogReader(self.filepath, self.handleLogUpdate)
        self.database = dbhandler.DatabaseHandler()
        self.playerName = 'Nieo'
        self.inGame = False
        self.deck = Deck("deck.txt")
        print(self.deck.decklist)
        self.board = Board(self.deck, 'huntard')
        self.logreader.start()
        sys.exit(self.app.exec_())

    def handleLogUpdate(self, type, data):
        if type == 'zone':
            boolean = True
            #print(data)
            if data[2] == "FRIENDLY DECK" and data[3] == "FRIENDLY HAND":
                print("Draw card", self.database.getCardName(data[1]))
                self.board.drawCard(data[0], data[1])
            elif data[2] == "FRIENDLY HAND" and data[3] == "FRIENDLY DECK":
                print("Muligan", self.database.getCardName(data[1]))
                self.board.mulligan(data[0])
            elif data[2] == "FRIENDLY HAND" and data[3] == "":
                print("Casting spell", self.database.getCardName(data[1]))
                self.board.castSpell(data[0])
            elif data[3] == "FRIENDLY HAND":
                self.board.hand.addCard(data[0], data[1])
                print("Adding card to hand", self.database.getCardName(data[1]))
            elif data[2] == "FRENDLY HAND" and data[3] == "FRIENDLY DECK":
                print("Place card in deck", self.logreader.getCardName(data[1]))
                self.board.deckSize += 1
            elif data[3] == "FRIENDLY DECK":
                print("Putting card in deck")
                self.board.deckSize += 1
            elif data[2] == "FRIENDLY HAND" and data[3] == "FRIENDLY PLAY":
                print("Friendly minion played", self.database.getCardName(data[1]))
                self.board.playMinion(data[0])
            elif data[2] == "FRIENDLY PLAY" and data[3] == "FRIENDLY GRAVEYARD":
                print("Friendly minion died", self.database.getCardName(data[1]))
            elif data[2] == "OPPOSING DECK" and data[3] == "OPPOSING HAND":
                print("OPPOSING draw")
                self.board.enemyDrawCard()
            elif data[2] == "OPPOSING HAND" and data[3] == "OPPOSING DECK":
                print("OPPOSING muligan")
                self.board.enemyDeckSize += 1
                self.board.enemyHandSize -= 1
            elif data[3] == "OPPOSING HAND":
                print("Adding card to opponents hand")
                self.board.enemyHandSize += 1
            elif data[3] == "OPPOSING DECK":
                print("Adding card to opponents deck", data)
                self.board.enemyDeckSize += 1
            elif data[2] == "OPPOSING HAND" and data[3] == "OPPOSING PLAY":
                self.board.enemyPlayCard(data[1])
                print("OPPOSING played minion", self.database.getCardName(data[1]))
            elif data[2] == "OPPOSING PLAY" and data[3] == "OPPOSING GRAVEYARD":
                print("OPPOSING minion died", self.database.getCardName(data[1]))
            else:
                print("Cant handle yet..", data)
                boolean = False
            if boolean:
                print(self.board)
        elif type =='playState':
            #print(self.inGame, data)
            #print("playState", data)
            if data == "CREATE_GAME" and not self.inGame:
                self.inGame = True
                #Starting a new game
                print("playState", data)
                print("Starting new game")
                self.board.initGame(self.deck)
                print(self.board)
            elif data[2] =='WON':
                self.inGame = False
                print(data[0] , " won")
                print(self.board)
if __name__ == '__main__':
    Inn()
