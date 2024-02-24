# calculator_cli.py
import argparse

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

def main():
    parser = argparse.ArgumentParser(description='A simple calculator.')
    parser.add_argument('x', type=float, help='First number')
    parser.add_argument('y', type=float, help='Second number')
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help='Operation')

    args = parser.parse_args()

    if args.operation == 'add':
        print("Result:", add(args.x, args.y))
    elif args.operation == 'subtract':
        print("Result:", subtract(args.x, args.y))
    elif args.operation == 'multiply':
        print("Result:", multiply(args.x, args.y))
    elif args.operation == 'divide':
        try:
            print("Result:", divide(args.x, args.y))
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
