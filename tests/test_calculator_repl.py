from app.calculator_repl import CalculatorFacade, CalculatorREPL

def test_calculator_facade_operations():
    facade = CalculatorFacade()
    assert facade.execute_operation("add", 2, 3) == 5.0
    assert facade.execute_operation("subtract", 10, 4) == 6.0
    assert len(facade.show_history()) == 2

    assert facade.undo() == "Undo successful."
    assert len(facade.show_history()) == 1

    assert facade.redo() == "Redo successful."
    assert len(facade.show_history()) == 2

    assert facade.clear_history() == "History cleared."
    assert len(facade.show_history()) == 0

    assert facade.undo() == "Undo successful."
    assert len(facade.show_history()) == 2

def test_calculator_facade_empty_undo_redo():
    facade = CalculatorFacade()
    assert facade.undo() == "Nothing to undo."
    assert facade.redo() == "Nothing to redo."

def test_calculator_facade_load_history():
    facade = CalculatorFacade()
    facade.load_history()
    assert isinstance(facade.history, list)

def test_history_capacity_overflow():
    facade = CalculatorFacade()
    from app.calculator_config import CalculatorConfig
    CalculatorConfig.MAX_HISTORY_SIZE = 2
    
    facade.execute_operation("add", 1, 1)
    facade.execute_operation("add", 2, 2)
    facade.execute_operation("add", 3, 3)
    
    assert len(facade.show_history()) == 2

def test_repl_instantiation():
    repl = CalculatorREPL()
    assert repl.facade is not None
