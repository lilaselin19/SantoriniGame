from game import Game
import sys

class Menu():
    def scoreSection(self):
        if self.scoreDisplay == "on":
            return f", ({self._game._activePlayer.getScores()})"
        else:
            return ""

    def handleURN(self):
        print("undo, redo, or next")
        inr = input("")
        while inr not in ["undo","redo","next"]:
            print("undo, redo, or next")
            inr = input("")
        # handle this at some point

    def run(self):
        while True:
            print(self._game._board)
            if self.undoRedo == "on":
                self.handleURN()
            print(f"Turn: {self._game._turnNumber}, {self._game._activePlayer}{self.scoreSection()}")
            self._game._activePlayer.doMove()
            self._game.nextTurn()

    def __init__(self, whiteType,blueType,undoRedo,scoreDisplay):
        self._game = Game(whiteType,blueType)
        self.undoRedo = undoRedo
        self.scoreDisplay = scoreDisplay


def getEl(list, index, default):
    return list[index] if index < len(list) else default

if __name__ == "__main__":
    args = sys.argv
    men = Menu(getEl(args,1,"human"),getEl(args,2,"human"),getEl(args,3,"off"),getEl(args,4,"off"))
    men.run()