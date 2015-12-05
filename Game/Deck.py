class Deck(object):
    """docstring for Deck"""
    def __init__(self, filepath):
        self.decklist = []
        self.buildFromFilePath(filepath)

    def drawCard(self, cardid):
        #self.decklist.remove(cardid)
        self.decklist.pop()

    def buildFromFilePath(self, filepath):
        deckFile = open(filepath, 'r')
        line = deckFile.readline()
        while(line):
            data = line.split(',')
            for i in range(int(data[0])):
                self.decklist.append(data[1])
            line = deckFile.readline()

    def size(self):
        return len(self.decklist)

    def addCard(self, cardid):
        self.decklist.append(cardid)
