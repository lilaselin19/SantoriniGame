import game
class Caretaker:
    def __init__(self,menu):
        self.menu = menu
        self.mementos = [self.menu.game.save()]

    def saveNext(self, turnNum):
        # print("saving")
        self.mementos = self.mementos[:turnNum]
        self.mementos.append(self.menu.game.save())
        # print(f"fullarr{self.mementos[idx].getTurnNumber()}")

    def undo(self, turnNum):
        idx = max(turnNum - 2, 0)
        # print(self.mementos)
        # print(f"fullarr{ self.mementos}")

        return self.mementos[idx]

    def redo(self, turnNum):
        idx = min(turnNum, len(self.mementos)-1)
        # print(f"fullarr{self.mementos}")
        return self.mementos[idx]

