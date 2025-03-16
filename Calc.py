import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def main():
    if len(sys.argv) != 4:
        print("Использование: python calc.py <число1> <операция> <число2>")
        print("Пример: python calc.py 5 + 3")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        operation = sys.argv[2]
        b = float(sys.argv[3])

        if operation == '+':
            result = add(a, b)
        elif operation == '-':
            result = subtract(a, b)
        elif operation == '*':
            result = multiply(a, b)
        elif operation == '/':
            result = divide(a, b)
        else:
            print("Неверная операция. Используйте +, -, *, /")
            sys.exit(1)

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: Введите числа корректно.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
