# Enhanced Calculator Application with Advanced Design Patterns and Pandas

A modular Python command-line calculator utilizing advanced object-oriented design patterns, persistent data storage with Pandas, and automated CI/CD via GitHub Actions.

## Setup & Running
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m app.calculator_repl
pytest --cov=app tests/
```bash
cat << 'EOF' > app/exceptions.py
class CalculatorError(Exception):
    pass

class InvalidInputError(CalculatorError):
    pass

class OperationError(CalculatorError):
    pass
