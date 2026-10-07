from app.calculator_config import CalculatorConfig
from app.operations import OperationFactory
from app.calculation import Calculation
from app.history import HistorySubject, HistoryManager, AutoSaveObserver
from app.calculator_memento import HistoryCaretaker
from app.input_validators import validate_number
from app.exceptions import CalculatorError

class CalculatorFacade(HistorySubject):
    def __init__(self):
        super().__init__()
        self.history = []
        self.history_manager = HistoryManager()
        self.caretaker = HistoryCaretaker()

        if CalculatorConfig.AUTO_SAVE:
            self.attach(AutoSaveObserver(self.history_manager))

    def load_history(self):
        self.history = self.history_manager.load_history()

    def execute_operation(self, op_name: str, a: float, b: float) -> float:
        operation = OperationFactory.get_operation(op_name)
        result = round(operation.execute(a, b), CalculatorConfig.PRECISION)
        
        self.caretaker.save_state(self.history)
        calc = Calculation(op_name, a, b, result)
        self.history.append(calc)

        if len(self.history) > CalculatorConfig.MAX_HISTORY_SIZE:
            self.history.pop(0)

        self.notify("add", {"history": self.history})
        return result

    def show_history(self):
        return [c.to_dict() for c in self.history]

    def clear_history(self):
        self.caretaker.save_state(self.history)
        self.history.clear()
        self.notify("clear", {"history": self.history})
        return "History cleared."

    def undo(self):
        prev = self.caretaker.undo(self.history)
        if prev is not None:
            self.history = prev
            self.notify("undo", {"history": self.history})
            return "Undo successful."
        return "Nothing to undo."

    def redo(self):
        nxt = self.caretaker.redo(self.history)
        if nxt is not None:
            self.history = nxt
            self.notify("redo", {"history": self.history})
            return "Redo successful."
        return "Nothing to redo."

class CalculatorREPL:
    def __init__(self):
        self.facade = CalculatorFacade()

    def start_repl(self):  # pragma: no cover
        self.facade.load_history()
        print("Calculator REPL started. Type 'help' for options, 'exit' to quit.")
        
        while True:
            try:
                user_input = input("calc> ").strip()
                if not user_input:
                    continue
                if user_input == "exit":
                    print("Goodbye!")
                    break

                parts = user_input.split()
                cmd = parts[0].lower()

                if cmd == "help":
                    print("Available commands: add, subtract, multiply, divide, power, root, history, clear, undo, redo, save, load, exit")
                elif cmd in ["add", "subtract", "multiply", "divide", "power", "root"]:
                    if len(parts) < 3:
                        print("Usage: <operation> <num1> <num2>")
                        continue
                    a = validate_number(parts[1])
                    b = validate_number(parts[2])
                    res = self.facade.execute_operation(cmd, a, b)
                    print(f"Result: {res}")
                elif cmd == "history":
                    print(self.facade.show_history())
                elif cmd == "clear":
                    print(self.facade.clear_history())
                elif cmd == "undo":
                    print(self.facade.undo())
                elif cmd == "redo":
                    print(self.facade.redo())
                elif cmd == "save":
                    self.facade.history_manager.save_history(self.facade.history)
                    print("History saved.")
                elif cmd == "load":
                    self.facade.load_history()
                    print("History loaded.")
                else:
                    print(f"Unknown command: {cmd}")
            except CalculatorError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":  # pragma: no cover
    repl = CalculatorREPL()
    repl.start_repl()
