import pytest
import subprocess
from Calc import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(10, 10) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(10, 5) == 2
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)  # Проверка деления на ноль

def test_cli():
    result = subprocess.run(['python', 'Calc.py', '5', '+', '3'], capture_output=True, text=True)
    assert "Результат: 8.0" in result.stdout

    result = subprocess.run(['python', 'Calc.py', '10', '/', '2'], capture_output=True, text=True)
    assert "Результат: 5.0" in result.stdout

    result = subprocess.run(['python', 'Calc.py', '4', '*', '3'], capture_output=True, text=True)
    assert "Результат: 12.0" in result.stdout

    result = subprocess.run(['python', 'Calc.py', '6', '-', '2'], capture_output=True, text=True)
    assert "Результат: 4.0" in result.stdout

    result = subprocess.run(['python', 'Calc.py', '5', '/', '0'], capture_output=True, text=True)
    assert "Ошибка:" in result.stdout
