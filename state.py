import copy


def findState(inputText):
    if inputText == "next":
        state = next_state
    elif inputText == "undo":
        state = undo_state
    elif inputText == "redo":
        state = next_state
    else:
        state = input_state
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
        menu.caretaker.saveNext(menu.game.getTurnNumber())
        menu.game.nextTurn()

        menu.state = inputState()

class undoState(menuState):
    def process(self, menu):
        menu.game = copy.deepcopy(menu.caretaker.undo(menu.game.getTurnNumber()))
        menu.game.nextTurn()
        menu.state = inputState()

class redoState(menuState):
    def process(self, menu):
        menu.game = copy.deepcopy(menu.caretaker.redo(menu.game.getTurnNumber()))
        menu.game.nextTurn()
        menu.state = inputState()


input_state = inputState()
next_state = nextState()
undo_state = undoState()
redo_state = redoState()
