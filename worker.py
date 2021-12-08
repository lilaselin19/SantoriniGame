from board import *
from square import *
from exceptions import *

class Worker:

    xEffect = {
        "n": 0, "ne": 1, "e": 1, "se": 1, "s": 0, "sw": -1, "w": -1, "nw": -1
    }

    yEffect = {
        "n": -1, "ne": -1, "e": 0, "se": 1, "s": 1, "sw": 1, "w": 0, "nw": -1
    }

    innerRing = ([1,1], [2,1], [3,1], [3,2], [3,3], [2,3], [1,3], [1,2])
    outerRing = ([0,0], [0,1], [0,2], [0,3], [0,4], [1,4], [2,4], [3,4],
              [4,4], [4,3], [4,2], [4,1], [4,0], [3,0], [2,0], [1,0])

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

    def _distanceTo(self, otherWorker):
        dx = abs(self._x - otherWorker._x)
        dy = abs(self._y - otherWorker._y)
        return (dx**2 + dy**2)**0.5

    def _getDestinationSquare(self, direction):
        if direction not in Worker.xEffect:
            raise InvalidDirectionError
        destinationX = self._x + Worker.xEffect[direction]
        destinationY = self._y + Worker.yEffect[direction]
        destinationSquare = self._board.getSquare(destinationX, destinationY)
        return destinationSquare, destinationX, destinationY

    def checkValidMove(self, direction):
        destinationSquare, x, y = self._getDestinationSquare(direction)
        if self._currentSquare.canMoveTo(destinationSquare):
            return True

        raise InvalidMoveError

    def checkValidBuild(self, direction):
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
        self._level = self._currentSquare.getLevel()

    def build(self, direction):
        destinationSquare, x, y = self._getDestinationSquare(direction)
        destinationSquare.build()

    def hasWon(self):
        if self._level == 3:
            return True
        return False

    def getScore(self,w1,w2):
        heightScore = self._level
        if [self._x, self._y] in Worker.outerRing:
            centerScore = 0
        elif [self._x, self._y] in Worker.innerRing:
            centerScore = 1
        else:
            centerScore = 2
        distanceScore = 8 - min(self._distanceTo(w1),self._distanceTo(w2))
        return heightScore + centerScore + distanceScore
