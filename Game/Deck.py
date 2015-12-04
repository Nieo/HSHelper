class Deck(object):
    """docstring for Deck"""
    def __init__(self, filepath):
        self.cards = []
        self.buildFromFilePath(filepath)

    def drawCard(self, cardid):
        self.cards.remove(cardid)
    
    def buildFromFilePath(self, filepath):
        deckFile = open(filepath, 'r')
        line = deckFile.readline()
        while(line):
            data = line.split(',')
            for i in range(int(data[0])):
                self.cards.append(data[1])
            line = deckFile.readline()