class Square:
    def __init__(self):
        self._workerName = " "
        self._level = 0

    def __repr__(self):
        return str(self._level) + self._workerName

    def build(self):
        if self._level < 4 and self._workerName == " ":
            self._level = self._level + 1
            return True
        return False

    def addWorker(self, name):
        self._workerName = name
