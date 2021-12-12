from game import Game
from memento import *
import sys


class Menu:
    def scoreSection(self):
        if self.scoreDisplay == "on":
            return f", ({self._game.activePlayer.getStringScores()})"
        else:
            return ""

    def run(self):
        while True:
            print(self._game)
            print(f"Turn: {self._game.getTurnNumber()}, {self._game.activePlayer}{self.scoreSection()}")
            if self.undoRedo == "on":
                print("undo, redo, or next")
                self.state = input("")
                while self.state not in ["undo", "redo", "next"]:
                    print("undo, redo, or next")
                    self.state = input("")
                if self.state == "undo":
                    self._game = self.caretaker.undo()
                    continue
                elif self.state == "redo":
                    self._game = self.caretaker.redo()
                    continue
                elif self.state == "next":
                    pass
            self._game.hasWon()
            self._game.activePlayer.doMove()
            if self.state == "next":
                # print("saving...")
                self.caretaker.saveNext()
            self._game.nextTurn()

    def __init__(self, whiteType,blueType,undoRedo,scoreDisplay):
        self._game = Game(whiteType,blueType)
        self.undoRedo = undoRedo
        self.scoreDisplay = scoreDisplay
        self.caretaker = Caretaker(self)


def getEl(myList, index, default):
    """Returns element of list myList at location index.
        If element at that index does not exist, return default"""
    return myList[index] if index < len(myList) else default


if __name__ == "__main__":
    args = sys.argv
    men = Menu(getEl(args,1,"human"),getEl(args,2,"human"),getEl(args,3,"off"),getEl(args,4,"off"))
    men.run()