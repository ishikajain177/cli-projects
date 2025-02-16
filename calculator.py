import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def exponentiate(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(a)

def calculator_menu():
    print("\nSimple Python Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation (a^b)")
    print("6. Square Root")
    print("7. Exit")

def main():
    while True:
        calculator_menu()
        choice = input("Choose an operation (1-7): ")

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                
                if choice == "1":
                    print(f"Result: {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {divide(num1, num2)}")
                elif choice == "5":
                    print(f"Result: {exponentiate(num1, num2)}")
            except ValueError:
                print("Error: Please enter valid numbers.")
        
        elif choice == "6":
            try:
                num = float(input("Enter the number: "))
                print(f"Result: {square_root(num)}")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == "7":
            print("Closing Calculator")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
