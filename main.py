from game import Game
import sys


class Menu:
    def scoreSection(self):
        if self.scoreDisplay == "on":
            return f", ({self._game.activePlayer.getStringScores()})"
        else:
            return ""

    def handleURN(self):
        """Handles Undo/ Redo/ Next"""
        # TODO implement this
        print("undo, redo, or next")
        inr = input("")
        while inr not in ["undo","redo","next"]:
            print("undo, redo, or next")
            inr = input("")
        # handle this at some point

    def run(self):
        while True:
            print(self._game)
            if self.undoRedo == "on":
                self.handleURN()
            print(f"Turn: {self._game.getTurnNumber()}, {self._game.activePlayer}{self.scoreSection()}")
            self._game.hasWon()
            self._game.activePlayer.doMove()
            self._game.nextTurn()

    def __init__(self, whiteType,blueType,undoRedo,scoreDisplay):
        self._game = Game(whiteType,blueType)
        self.undoRedo = undoRedo
        self.scoreDisplay = scoreDisplay


def getEl(myList, index, default):
    """Returns element of list myList at location index.
        If element at that index does not exist, return default"""
    return myList[index] if index < len(myList) else default


if __name__ == "__main__":
    args = sys.argv
    men = Menu(getEl(args,1,"human"),getEl(args,2,"human"),getEl(args,3,"off"),getEl(args,4,"off"))
    men.run()