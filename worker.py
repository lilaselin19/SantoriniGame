import board

class Worker:
    def __init__(self, name, myPlayer, x, y, myBoard):
        self._name = name
        self._myPlayer = myPlayer
        self._x = x
        self._y = y
        self._myBoard = myBoard
        self._level = 0

        self._myBoard.getSquare(x,y).addWorker(self._name)

    def move(self, direction):
        # what pattern can be used instead of giant if else chain?
        # ie to replace
            # if direction == "n":
                #y = y - 1
        raise NotImplementedError

    def build(self, direction):
        # same thing as build
        raise NotImplementedError