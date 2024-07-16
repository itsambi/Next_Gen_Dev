def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

while True:
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    choice = input("Choose an operation: ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
            operation = "Addition"
        elif choice == "2":
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == "3":
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == "4":
            result = divide(num1, num2)
            operation = "Division"

        print(f"{operation} result: {result:.2f}")
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
