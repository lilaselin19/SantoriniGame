from worker import *
from board import *
from exceptions import *

import random

directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

inverseDirection = {
    "n":"s", "ne":"sw", "e":"w", "se":"nw", "s":"n", "sw":"ne", "w":"e", "nw":"se"
}

class Player:

    def __init__(self, playerType, playerName, gameboard):
        self._workers = list()
        self._board = gameboard

        if playerType == "human":
            self.doMove = self._humanStrategy
        elif playerType == "random":
            self.doMove = self._randomStrategy
        else:
            self.doMove = self._heuristicStrategy

        self._playerName = playerName
        if playerName == "white":
            self._createWorker("A", 1, 3)
            self._createWorker("B", 3, 1)

        else:
            self._createWorker("Y", 1, 1)
            self._createWorker("Z", 3, 3)

    def __repr__(self):
        return f"{self._playerName} ({self._workers[0]}{self._workers[1]})"

    def setOpponent(self, opponent):
        self._opponent = opponent

    def hasWon(self):
        for w in self._workers:
            if w.hasWon():
                return True
        return False

    def printWinMessage(self):
        print(f"{self._playerName} has won")

    def _createWorker(self, name, x, y):
        w = Worker(name, self, x, y, self._board)
        self._workers.append(w)

    def _selectWorker(self, name):
        for w in self._workers:
            if repr(w) == name:
                return w
        raise InvalidWorkerError()

    def getAllPossibleMoves(self):
        """Enumerates and returns all possible moves,
        each move is a tuple of the format [worker, moveDirection, buildDirection]"""
        possibleMoves = list()
        for w in self._workers:
            moves = list()
            for direction in directions:
                try:
                    w.checkValidMove(direction)
                    moves.append(direction)
                except (InvalidMoveError, InvalidSquareError):
                    pass

            for moveDirection in moves:
                w.move(moveDirection)
                for direction in direction:
                    try:
                        w.checkValidBuild(direction)
                        possibleMoves.append([w, moveDirection, direction])
                    except (InvalidBuildError, InvalidSquareError):
                        pass
                w.move(inverseDirection[moveDirection])

        return possibleMoves

    def _calculateHeuristic(self):
        score = 0
        for w in self._workers:
            score += w.getScore(self._opponent._workers[0], self._opponent._workers[1])
        return score

    def _humanStrategy(self):
        w = None
        validStep = False
        while not validStep:
            try:
                worker = input("Select a worker to move\n")
                w = self._selectWorker(worker)
                validStep = True
            except InvalidWorkerError:
                try:
                    self._opponent._selectWorker(worker)
                    print("That is not your worker")
                except InvalidWorkerError:
                    print("Not a valid worker")

        validStep = False
        while not validStep:
            try:
                moveDirection = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
                validStep = w.checkValidMove(moveDirection)
            except InvalidDirectionError:
                print("Not a valid direction")
            except (InvalidMoveError, InvalidSquareError):
                print(f"Cannot move {moveDirection}")

        w.move(moveDirection)
        validStep = False
        while not validStep:
            try:
                buildDirection = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
                validStep = w.checkValidBuild(buildDirection)
            except InvalidDirectionError:
                print("Not a valid direction")
            except (InvalidBuildError, InvalidSquareError):
                print(f"Cannot build {buildDirection}")

        w.build(buildDirection)

    def _randomStrategy(self):
        possibleMoves = self.getAllPossibleMoves()
        w, moveDirection, buildDirection = random.choice(possibleMoves)
        print(f"{w},{moveDirection},{buildDirection}")
        w.move(moveDirection)
        w.build(buildDirection)

    def _heuristicStrategy(self):
        possibleMoves = self.getAllPossibleMoves()
        heuristics = list()
        for move in possibleMoves:
            w = move[0]
            moveDirection = move[1]
            w.move(moveDirection)
            heuristics.append(self._calculateHeuristic())
            w.move(inverseDirection[moveDirection])

        bestMove = possibleMoves[heuristics.index(max(heuristics))]
        bestMove[0].move(bestMove[1])
        bestMove[0].build(bestMove[2])