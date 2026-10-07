class CalculatorError(Exception):
    """Base exception class for calculator applications."""
    pass

class InvalidInputError(CalculatorError):
    """Raised when user input fails validation."""
    pass

class OperationError(CalculatorError):
    """Raised when an error occurs during calculation execution."""
    pass
