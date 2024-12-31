mkdir -p ./sample_project ./sample_project/src ./sample_project/test

cat <<EOL > ./sample_project/requirements.txt
## test package ##
pytest        # Core pytest framework
pytest-xdist  # Supports parallel test execution
pytest-mock   # Simplifies the use of mock objects in tests
pytest-flake8 # Checks code style and quality to improve code standards
pytest-html   # Outputs test results as HTML reports
pytest-cov    # measuring test coverage
lizard        # Code complexity analysis tool

## sut package ##
requests
EOL

cat <<EOL > ./sample_project/src/main.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b  # Intentional division by zero

def branch(a, b):
    if (a == True) and (b == True):
        return True
    else:
        return False
EOL

cat <<EOL > ./sample_project/test/test_main.py
import pytest
from src.main import add, sub, mul, div, branch

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_sub():
    assert sub(2, 1) == 1
    assert sub(2, 2) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 3) == -3

def test_div():
    assert div(6, 2) == 3
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_branch():
    assert branch(True, True) is True
    assert branch(True, False) is False
    assert branch(False, False) is False
EOL

cat <<EOL > ./sample_project/test/conftest.py
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/*"))
EOL

