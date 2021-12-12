class Square:
    def __init__(self):
        self._workerName = " "
        self.level = 0

    def __repr__(self):
        return str(self.level) + self._workerName

    def canBuildOn(self):
        if self.level < 4 and self._workerName == " ":
            return True
        return False

    def canMoveTo(self, otherSquare):
        if otherSquare.level - 1 <= self.level and otherSquare.level < 4 and otherSquare._workerName == " ":
            return True
        return False

    def build(self):
        if self.level < 4 and self._workerName == " ":
            self.level = self.level + 1
            return True
        return False

    def addWorker(self, name):
        self._workerName = name

    def removeWorker(self):
        self._workerName = " "

    def getLevel(self):
        return self.level
