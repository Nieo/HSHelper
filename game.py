import logging
from Database.dbhandler import DatabaseHandler


class Game():

    """Model for a game"""

    def __init__(self):
        super(Game, self).__init__()
        self.database = DatabaseHandler()
        self.opponentPlays = {}

        logging.debug("Created a game")

    def opponentPlay(self, cardid):
        if cardid in self.opponentPlays:
            self.opponentPlays[cardid] += 1
        else:
            self.opponentPlays[cardid] = 1
        self.updateOpponentPlay.emit(self.database.getCardName(cardid))

    def pushOpponentPlay(self):
        for cardid in self.opponentPlays:
            for i in range(0, self.opponentPlays[cardid]):
                self.updateOpponentPlay.emit(self.database.getCardName(cardid))
