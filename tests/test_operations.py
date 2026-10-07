import pytest
from app.operations import OperationFactory
from app.exceptions import OperationError

@pytest.mark.parametrize("op_name, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 10, 4, 6),
    ("multiply", 3, 4, 12),
    ("divide", 8, 2, 4),
    ("power", 2, 3, 8),
    ("root", 16, 2, 4),
])
def test_operations_success(op_name, a, b, expected):
    operation = OperationFactory.get_operation(op_name)
    assert operation.execute(a, b) == expected

def test_divide_by_zero():
    operation = OperationFactory.get_operation("divide")
    with pytest.raises(OperationError):
        operation.execute(10, 0)

def test_even_root_negative():
    operation = OperationFactory.get_operation("root")
    with pytest.raises(OperationError):
        operation.execute(-16, 2)

def test_unknown_operation():
    with pytest.raises(OperationError):
        OperationFactory.get_operation("modulus")
