# Simple calculator

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

# Main program
def main():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("Choose operation:")
    print(" +  for addition")
    print(" -  for subtraction")
    print(" *  for multiplication")
    print(" /  for division")

    operation = input("Enter operation: ")

    result = calculate(num1, num2, operation)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
