from app.calculation import Calculation

def test_calculation_creation():
    calc = Calculation("add", 2.0, 3.0, 5.0, "2026-10-07 12:00:00")
    data = calc.to_dict()
    assert data["operation"] == "add"
    assert data["operand1"] == 2.0
    assert data["operand2"] == 3.0
    assert data["result"] == 5.0
    assert data["timestamp"] == "2026-10-07 12:00:00"
