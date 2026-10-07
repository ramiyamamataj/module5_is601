import pytest
from app.input_validators import validate_number, validate_command
from app.exceptions import InvalidInputError

@pytest.mark.parametrize("input_str, expected", [
    ("10", 10.0),
    ("-5.5", -5.5),
    ("0", 0.0),
])
def test_validate_number_valid(input_str, expected):
    assert validate_number(input_str) == expected

@pytest.mark.parametrize("invalid_str", ["abc", "10.10.10", "10000000"])
def test_validate_number_invalid(invalid_str):
    with pytest.raises(InvalidInputError):
        validate_number(invalid_str)

def test_validate_command():
    allowed = ["add", "subtract", "exit"]
    assert validate_command("  ADD ", allowed) == "add"
    with pytest.raises(InvalidInputError):
        validate_command("invalid_cmd", allowed)
