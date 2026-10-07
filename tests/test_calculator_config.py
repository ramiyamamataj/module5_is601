import os
from app.calculator_config import CalculatorConfig

def test_config_defaults():
    assert CalculatorConfig.MAX_HISTORY_SIZE == 100
    assert CalculatorConfig.DEFAULT_ENCODING == "utf-8"
    assert CalculatorConfig.PRECISION == 4
