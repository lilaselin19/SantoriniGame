import worker
import board

class Player:
    def __init__(self, playerType, playerNumber, myBoard):
        self._workers = list()
        self._myBoard = myBoard
        if playerType == "human":
            self._decideMoveStrategy = self._humanStrategy
        elif playerType == "random":
            self._decideMoveStrategy = self._randomStrategy
        else:
            self._decideMoveStrategy = self._heuristicStrategy

        if playerNumber == 0:
            self._createWorker("A", 1, 3)
            self._createWorker("B", 3, 1)

        else:
            self._createWorker("Y", 1, 1)
            self._createWorker("Z", 3, 3)

    def _createWorker(self, name, x, y):
        w = worker.Worker(name, self, x, y, self._myBoard)
        self._workers.append(w)

    def _selectWorker(self, name):
        for w in self._workers:
            if w.getName() == name:
                return w
        raise NoWorkerError()

    def doMove(self):
        direction = self._decideMoveStrategy()
        raise NotImplementedError

    def _getAllPossibleMoves(self):
        raise NotImplementedError

    def _calculateHeuristic(self):
        raise NotImplementedError

    def _humanStrategy(self):
        raise NotImplementedError

    def _randomStrategy(self):
        raise NotImplementedError

    def _heuristicStrategy(self):
        raise NotImplementedError

class NoWorkerError(Exception):
    pass