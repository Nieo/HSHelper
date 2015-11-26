import re


class LogReader():

    """docstring for LogReader"""

    def __init__(self, logfile, handler):
        self.logfile = open(logfile, 'r')
        self.zoneChange = re.compile(
            ' id=(\d+)[^\[]*cardId=(\w+).*zone from (.*) -> (.*)')
        self.playState = re.compile(
            'TAG_CHANGE Entity=(\w+).*tag=PLAYSTATE value=(\w+)')

        self.handler = handler

    def readLog(self):
        where = self.logfile.tell()
        line = self.logfile.readline()
        if line:
            zone = self.zoneChange.findall(line)
            result = self.playState.findall(line)
            if zone != []:
                self.handler('zone', zone[0])
            elif result:
                self.handler('playState', result[0])
        else:
            self.logfile.seek(where)

    def start(self):
        print("Called start")
        while True:
            self.readLog()
