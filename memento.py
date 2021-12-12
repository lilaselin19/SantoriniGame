import game
class Caretaker:
    def __init__(self,menu):
        self.menu = menu
        self.mementos = [self.menu.game.save()]
        self.current = 0

    def saveNext(self):
        self.current += 1
        self.mementos = self.mementos[:self.current]
        self.mementos.append(self.menu.game.save())
        # print(self.mementos)

    def undo(self):
        changed = False
        if self.current > 0:
            self.current-=1
            changed = True
        return self.mementos[self.current], changed

    def redo(self):
        changed = True
        self.current+=1
        if self.current>=len(self.mementos):
            self.current -= 1
            changed = False
        return self.mementos[self.current], changed
