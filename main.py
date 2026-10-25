def add(a, b):
    try:
        return a + b
    except TypeError:
        raise TypeError("Both must be numbers.")
    except ValueError:
        raise ValueError("Invalid. enter valid numbers.")

def subtract(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Both must be numbers.")
    except ValueError:
            raise ValueError("Invalid. enter valid numbers.")

def multiply(a, b):
    try:
        return a * b
    except TypeError:
        raise TypeError("Both must be numbers.")
    except ValueError:
        raise ValueError("Invalid. enter valid numbers.")
    
def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Can't divide by zero.")
        return a / b
    except TypeError:
        raise TypeError("Both must be numbers.")
    except ValueError:
        raise ValueError("Invalid. enter valid numbers.")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Add: {add(a, b)}")
print(f"Subtract: {subtract(a, b)}")
print(f"Multiply: {multiply(a, b)}")
print(f"Divide: {divide(a, b)}")
