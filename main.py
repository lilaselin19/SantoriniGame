from game import Game
import sys

class Menu():
    def run(self):
        while True:
            print(self._game._board)
            break

    def __init__(self, whiteType,blueType,undoRedo,scoreDisplay):
        print(whiteType,blueType,undoRedo,scoreDisplay)
        self._game = Game(whiteType,blueType)
        self.undoRedo = undoRedo
        self.scoreDisplay = scoreDisplay


def getEl(list, index, default):
    return list[index] if index < len(list) else default

if __name__ == "__main__":
    args = sys.argv
    men = Menu(getEl(args,1,"human"),getEl(args,2,"human"),getEl(args,3,"off"),getEl(args,4,"off"))
    print("pass")
    men.run()