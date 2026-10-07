import math
from app.exceptions import OperationError

class Operation:
    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError  # pragma: no cover

class AddOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b

class SubtractOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b

class MultiplyOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b

class DivideOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b

class PowerOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return math.pow(a, b)

class RootOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of negative number is undefined.")
        return math.pow(a, 1.0 / b)

class OperationFactory:
    _operations = {
        "add": AddOperation(),
        "subtract": SubtractOperation(),
        "multiply": MultiplyOperation(),
        "divide": DivideOperation(),
        "power": PowerOperation(),
        "root": RootOperation(),
    }

    @classmethod
    def get_operation(cls, op_name: str) -> Operation:
        op = cls._operations.get(op_name.lower())
        if not op:
            raise OperationError(f"Unknown operation strategy: '{op_name}'")
        return op
