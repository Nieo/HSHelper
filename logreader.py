import re


class LogReader():

    """docstring for LogReader"""

    def __init__(self, logfile, handler):
        self.logfile = open(logfile, 'r')
        # pos0 = id, pos1 = cardid, pos2 = startZone, pos3 = destinationZone
        self.zoneChange = re.compile(
            r"id=(\d+)[^\[]*cardId=(\w*).*zone from (.*) -> (.*)")

        self.playState = re.compile(
            r"TAG_CHANGE Entity=(\w+).*tag=(\w+) value=(\w+)")

        self.createGame = re.compile(r"(CREATE_GAME)")


#TAG_CHANGE Entity=GameEntity tag=TURN value=1

        self.handler = handler

    def readLog(self):
        where = self.logfile.tell()
        line = self.logfile.readline()
        if line:
            zone = self.zoneChange.findall(line)
            result = self.playState.findall(line)
            newGame = self.createGame.findall(line)
            if zone != []:
                self.handler('zone', zone[0])
            elif result:
                self.handler('playState', result[0])
            elif newGame:
                self.handler('playState', newGame[0])
        else:
            self.logfile.seek(where)

    def start(self):
        print("Called start")
        while True:
            self.readLog()
