# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    if operation == "add":
        print("Result:", add(x, y))
    elif operation == "subtract":
        print("Result:", subtract(x, y))
    elif operation == "multiply":
        print("Result:", multiply(x, y))
    elif operation == "divide":
        try:
            print("Result:", divide(x, y))
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation")
