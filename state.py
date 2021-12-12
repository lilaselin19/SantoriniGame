def findState(inputText):
    if inputText == "next":
        state = nextState()
    elif inputText == "undo":
        state = undoState()
    elif inputText == "redo":
        state = redoState()
    else:
        state = inputState()

    return state



class menuState:

    def process(self, menu):
        raise NotImplementedError


class inputState(menuState):
    def process(self, menu):
        print("undo, redo, or next")
        menu.state = findState(input(""))


class nextState(menuState):
    def process(self, menu):
        menu.game.hasWon()
        menu.game.activePlayer.doMove()
        menu.caretaker.saveNext()
        menu.game.nextTurn()
        menu.state = inputState()

class undoState(menuState):
    def process(self, menu):
        menu.game, changed = menu.caretaker.undo()
        if changed:
            menu.game.nextTurn()
        menu.state = inputState()

class redoState(menuState):
    def process(self, menu):
        menu.game, changed = menu.caretaker.redo()
        if changed:
            menu.game.nextTurn()
        menu.state = inputState()