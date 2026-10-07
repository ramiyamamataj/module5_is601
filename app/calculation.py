from datetime import datetime

class Calculation:
    def __init__(self, operation: str, operand1: float, operand2: float, result: float, timestamp: str = None):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp
        }
