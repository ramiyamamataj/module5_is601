import os
import pandas as pd
from app.calculator_config import CalculatorConfig
from app.calculation import Calculation

class Observer:
    def update(self, event_type: str, data: dict):
        raise NotImplementedError  # pragma: no cover

class HistorySubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event_type: str, data: dict):
        for observer in self._observers:
            observer.update(event_type, data)

class AutoSaveObserver(Observer):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def update(self, event_type: str, data: dict):
        if event_type in ["add", "clear", "undo", "redo"]:
            self.history_manager.save_history(data.get("history", []))

class HistoryManager:
    def __init__(self):
        self.history_dir = os.path.join(CalculatorConfig.BASE_DIR, "history")
        os.makedirs(self.history_dir, exist_ok=True)
        self.filepath = os.path.join(self.history_dir, "calc_history.csv")

    def save_history(self, calculations):
        try:
            data = [c.to_dict() for c in calculations]
            df = pd.DataFrame(data)
            df.to_csv(self.filepath, index=False, encoding=CalculatorConfig.DEFAULT_ENCODING)
        except Exception as e:
            raise RuntimeError(f"Failed to save CSV history: {e}")

    def load_history(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            df = pd.read_csv(self.filepath, encoding=CalculatorConfig.DEFAULT_ENCODING)
            calculations = []
            for _, row in df.iterrows():
                calc = Calculation(
                    operation=str(row['operation']),
                    operand1=float(row['operand1']),
                    operand2=float(row['operand2']),
                    result=float(row['result']),
                    timestamp=str(row['timestamp'])
                )
                calculations.append(calc)
            return calculations
        except Exception:
            return []
