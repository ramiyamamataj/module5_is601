from app.calculator_memento import HistoryCaretaker

def test_memento_undo_redo():
    caretaker = HistoryCaretaker()
    state1 = [1, 2]
    caretaker.save_state(state1)
    
    state2 = [1, 2, 3]
    undone = caretaker.undo(state2)
    assert undone == [1, 2]
    
    redone = caretaker.redo(undone)
    assert redone == [1, 2, 3]

def test_memento_empty_undo_redo():
    caretaker = HistoryCaretaker()
    assert caretaker.undo([]) is None
    assert caretaker.redo([]) is None
