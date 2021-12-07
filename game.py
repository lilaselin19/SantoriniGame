import boardimport copyimport playerclass Game:    def __init__(self, type1, type2):        '''Create a new game object'''        self._board = board.Board()        self._player1 = player.Player(type1,"white",self._board)        self._player2 = player.Player(type2,"blue",self._board)        self._player1.setOpponent(self._player2)        self._player2.setOpponent(self._player1)        self._turnNumber = 1        self.activePlayer = self._player1    def __repr__(self):        return repr(self._board)    def save(self):        '''Save a copy of the current game'''        # more efficient way to do this is to save only the necessary information        # that can be a TODO for later        return copy.deepcopy(self)    def nextTurn(self):        self.hasWon(self.activePlayer)        if self.activePlayer == self._player1:            self.activePlayer = self._player2        else:            self.activePlayer = self._player1        self._turnNumber +=1    def hasWon(self, player):        if player.hasWon():            player.printWinMessage()            quit()    def getTurnNumber(self):        return self._turnNumber