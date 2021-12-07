class Square:
    def __init__(self):
        self._workerName = " "
        self._level = 0

    def __repr__(self):
        return str(self._level) + self._workerName

    def canBuildOn(self):
        if self._level < 4 and self._workerName == " ":
            return True
        return False

    def canMoveTo(self, otherSquare):
        if otherSquare._level - 1 <= self._level and otherSquare._level < 4 and otherSquare._workerName == " ":
            return True
        return False


    def build(self):
        if self._level < 4 and self._workerName == " ":
            self._level = self._level + 1
            return True
        return False

    def addWorker(self, name):
        self._workerName = name

    def removeWorker(self):
        self._workerName = " "
