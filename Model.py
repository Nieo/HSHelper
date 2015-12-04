from Game.Board import Board
from logreader import LogReader
from Game.Deck import Deck
from Database import dbhandler

class Model(object):
    def __init__(self):
        self.filepath = 'C:\Program Files (x86)\Hearthstone\Hearthstone_Data\output_log.txt'
        self.logreader = LogReader(self.filepath, self.handleLogUpdate)
        self.database = dbhandler.DatabaseHandler()
        self.playerName = 'Boarman'
        self.deck = Deck("deck.txt")
        self.inGame = False
        print("astfs")
        print(self.deck.cards)
        board = Board(self.deck, 'huntard')        
        self.logreader.start()
        sys.exit(self.app.exec_())

    def handleLogUpdate(self, type, data):
        if type == 'zone':

        elif type =='playState':
            if data[1] == 'PLAYING' and not self.inGame:
                #Starting a new game
                board.initGame(self.deck)
                self.inGame = True
            elif data[1] =='WON' and self.inGame:
                self.inGame = False
                print(data[0] , " won")    
if __name__ == '__main__':
    Model()