"""
Project : Password Generator
Author  : Swati Ranjita Swain
Language: Python 3

Description:
Generates strong and secure random passwords based on
the user-defined password length.
"""

import random
import string


class PasswordGenerator:
    """Generates secure random passwords."""

    def __init__(self):
        self.characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

    def generate_password(self, length):
        if length < 4:
            raise ValueError(
                "Password length must be at least 4 characters."
            )

        password = ''.join(
            random.choice(self.characters)
            for _ in range(length)
        )

        return password


def get_password_length():
    """Get a valid password length from the user."""

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password must contain at least 4 characters.\n")
                continue

            return length

        except ValueError:
            print("Please enter a valid number.\n")


def main():
    print("=" * 45)
    print("        STRONG PASSWORD GENERATOR")
    print("=" * 45)

    generator = PasswordGenerator()

    while True:
        length = get_password_length()

        password = generator.generate_password(length)

        print("\nGenerated Password:")
        print(password)

        choice = input("\nGenerate another password? (Y/N): ").strip().lower()

        if choice != "y":
            print("\nThank you for using Password Generator.")
            break


if __name__ == "__main__":
    main()
