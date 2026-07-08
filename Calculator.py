"""
Project : Calculator
Author  : Swati Ranjita Swain
Language: Python 3

Description:
A professional command-line calculator that performs
basic arithmetic operations with proper input validation.
"""


class Calculator:
    """A simple calculator class."""

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2


def display_menu():
    print("\n" + "=" * 40)
    print("        PYTHON CALCULATOR")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=" * 40)


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")


def main():
    calculator = Calculator()

    while True:
        display_menu()

        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the Calculator.")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please try again.")
            continue

        num1, num2 = get_numbers()

        try:
            if choice == "1":
                result = calculator.add(num1, num2)
                operator = "+"

            elif choice == "2":
                result = calculator.subtract(num1, num2)
                operator = "-"

            elif choice == "3":
                result = calculator.multiply(num1, num2)
                operator = "*"

            else:
                result = calculator.divide(num1, num2)
                operator = "/"

            print(f"\nResult: {num1} {operator} {num2} = {result}")

        except ZeroDivisionError as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
