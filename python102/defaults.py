"""
Author: Almog Manor
Example of usage of default function parameters
"""


def add(num1, num2=5):
    return num1 + num2


def multiply(num1, num2=5, num3=10):
    return num1 * num2 * num3


def main():
    """entry point to the program
    """

    # num1 = 2, num2 = 4
    print(add(2, 4))
    # num1 = 3, num2 = 5
    print(add(3, 5))
    # num1 = 3, num2 = 5
    print(add(3))

    # num1 = 1, num2 = 2, num3 = 3
    print(multiply(1, 2, 3))
    # num1 = 1, num2 = 2, num3 = 10
    print(multiply(1, 2))
    # num1 = 1, num2 = 5, num3 = 7
    print(multiply(1, num3=7))
    # num1 = 1, num2 = 6, num3 = 9
    print(multiply(1, num3=9, num2=6))


if __name__ == "__main__":
    main()
