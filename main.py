from game import Game
from memento import *
from state import *
import sys


class Menu:
    def scoreSection(self):
        if self._scoreDisplay == "on":
            return f", ({self.game.activePlayer.getStringScores()})"
        else:
            return ""


    def run(self):
        while True:
            print(self.game)
            print(f"Turn: {self.game.getTurnNumber()}, {self.game.activePlayer}{self.scoreSection()}")


            if self.undoRedo == "on":
                while type(self.state) is inputState:
                    self.state.process(self)

            else:
                self.state = nextState()

            self.state.process(self)


    def __init__(self, whiteType,blueType,undoRedo,scoreDisplay):
        self.game = Game(whiteType,blueType)
        self.undoRedo = undoRedo
        self._scoreDisplay = scoreDisplay
        self.caretaker = Caretaker(self)
        self.state = inputState()


def getEl(myList, index, default):
    """Returns element of list myList at location index.
        If element at that index does not exist, return default"""
    return myList[index] if index < len(myList) else default


if __name__ == "__main__":
    args = sys.argv
    men = Menu(getEl(args,1,"human"),getEl(args,2,"human"),getEl(args,3,"off"),getEl(args,4,"off"))
    men.run()