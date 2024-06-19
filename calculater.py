def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero not possible."

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter choice (1/2/3/4): ")

    if operation == '1':
        result = add(num1, num2)
        print(f"The result is: {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"The result is: {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"The result is: {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result is: {result}")
    else:
        print("Invalid operation choice! Please enter a valid choice.")

if __name__ == "__main__":
    calculator()