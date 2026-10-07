import pytest
from app.exceptions import CalculatorError, InvalidInputError, OperationError

def test_exceptions():
    with pytest.raises(CalculatorError):
        raise InvalidInputError("Invalid input error occurred")
    
    with pytest.raises(CalculatorError):
        raise OperationError("Operation error occurred")
