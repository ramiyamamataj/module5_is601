class Memento:
    def __init__(self, state):
        self._state = list(state)

    def get_state(self):
        return list(self._state)

class HistoryCaretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save_state(self, current_history):
        self._undo_stack.append(Memento(current_history))
        self._redo_stack.clear()

    def undo(self, current_history):
        if not self._undo_stack:
            return None
        self._redo_stack.append(Memento(current_history))
        memento = self._undo_stack.pop()
        return memento.get_state()

    def redo(self, current_history):
        if not self._redo_stack:
            return None
        self._undo_stack.append(Memento(current_history))
        memento = self._redo_stack.pop()
        return memento.get_state()
