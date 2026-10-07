import os
from dotenv import load_dotenv

load_dotenv()

class CalculatorConfig:
    BASE_DIR = os.getenv("CALCULATOR_BASE_DIR", "data")
    MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
    AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
    PRECISION = int(os.getenv("CALCULATOR_PRECISION", "4"))
    MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000"))
    DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
