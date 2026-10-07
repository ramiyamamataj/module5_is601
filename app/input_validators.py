from app.exceptions import InvalidInputError
from app.calculator_config import CalculatorConfig

def validate_number(value_str: str) -> float:
    try:
        val = float(value_str)
    except ValueError:
        raise InvalidInputError(f"Invalid numeric input: '{value_str}'")

    if abs(val) > CalculatorConfig.MAX_INPUT_VALUE:
        raise InvalidInputError(f"Value {val} exceeds maximum permitted limit ({CalculatorConfig.MAX_INPUT_VALUE})")
        
    return val

def validate_command(command: str, allowed_commands: list) -> str:
    cleaned = command.strip().lower()
    if cleaned not in allowed_commands:
        raise InvalidInputError(f"Unknown command: '{command}'")
    return cleaned
