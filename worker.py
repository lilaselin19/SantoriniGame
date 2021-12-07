from board import *
from square import *

class Worker:

    xEffect = {
        "n": 0,
        "ne": 1,
        "e": 1,
        "se": 1,
        "s": 0,
        "sw": -1,
        "w": -1,
        "nw": -1
    }

    yEffect = {
        "n": -1,
        "ne": -1,
        "e": 0,
        "se": -1,
        "s": 1,
        "sw": 1,
        "w": 0,
        "nw": -1
    }

    def __init__(self, name, myPlayer, x, y, board):
        self._name = name
        self._myPlayer = myPlayer
        self._x = x
        self._y = y
        self._level = 0

        self._board = board
        self._currentSquare = self._board.getSquare(x,y)
        self._currentSquare.addWorker(self._name)

    def __repr__(self):
        return self._name

    def __eq__(self, other):
        if type(other) is Worker:
            if other._name == self._name:
                return True

        if other == self._name:
            return True

        return False

    def _getDestinationSquare(self, direction):
        destinationX = self._x + Worker.xEffect[direction]
        destinationY = self._y + Worker.yEffect[direction]
        destinationSquare = self._board.getSquare(destinationX, destinationY)
        return destinationSquare, destinationX, destinationY

    def checkValidMove(self, direction):
        if direction not in Worker.xEffect:
            raise InvalidMoveError
        destinationSquare, x, y = self._getDestinationSquare(direction)
        if self._currentSquare.canMoveTo(destinationSquare):
            return True

        raise InvalidMoveError

    def checkValidBuild(self, direction):
        if direction not in Worker.xEffect:
            raise InvalidMoveError
        destinationSquare, x, y = self._getDestinationSquare(direction)
        if destinationSquare.canBuildOn():
            return True

        raise InvalidBuildError

    def move(self, direction):
        destinationSquare, x, y = self._getDestinationSquare(direction)
        self._currentSquare.removeWorker()
        self._currentSquare = destinationSquare
        self._currentSquare.addWorker(self._name)
        self._x = x
        self._y = y

    def build(self, direction):
        destinationSquare, x, y = self._getDestinationSquare(direction)
        destinationSquare.build()


class InvalidMoveError(Exception):
    pass


class InvalidBuildError(Exception):
    pass
