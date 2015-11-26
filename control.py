import sys
import logging
import os
from Database import dbhandler
from logreader import LogReader


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Control():

    """Main controler"""

    def __init__(self):
        # Logreader
        self.filepath = '/Users/Nieo/Library/Logs/Unity/Player.log'
        self.logreader = LogReader(self.filepath, self.handleLogUpdate)
        self.database = dbhandler.DatabaseHandler()
        self.playerName = 'Nieo'
        self.logreader.start()

        sys.exit(self.app.exec_())

    def handleLogUpdate(self, type, data):
        if type == "zone":
            if data[2] == "OPPOSING HAND":
                print(self.database.getCardName(data[1]))
            else:
                pass
                # logging.debug(data)
        elif type == "playState":
            logging.debug(data)
            if data[1] == 'PLAYING' and data[0] == self.playerName:
                logging.info("New game starting")

            elif data[1] == 'WON':
                if data[0] == self.playerName:
                    print("------Victory------")
                    cls()
                    logging.info("You have won")
                else:
                    print("-----Defeat-----")
                    cls()
                    logging.info("You have lost")


if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    a = Control()
