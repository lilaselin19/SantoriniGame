import game
class NothingToRestoreException(Exception):
    pass

class Memento:
    def __init__(self):
        self.mementos = []
        self.current = -1

    def next(self):
        self.current+=1
        self.mementos[self.current] =
        self.mementos = self.mementos[:self.current]

    def undo(self):
        if len(self.mementos) == 0:
            raise NothingToRestoreException
        else:
            return

    def saveGame(self):
