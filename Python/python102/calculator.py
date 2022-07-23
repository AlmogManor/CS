"""
Author: Almog Manor
Calculator capable of: quadratic formula, factorial, fibonacci(n)
"""
from math import sqrt


def quadratic_formula():
    """x1, x2 = (-b + sqrt(b^2 - 4ac)) / 2a
    """
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    c = float(input("Enter c:"))

    discriminant = sqrt((b ** 2) - (4 * a * c))
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)

    print(f"x1: {x1}")
    print(f"x2: {x2}")


def factorial():
    """repetitive multiplication until 1, e.g:
       4! = 4 * 3 * 2 * 1
    """
    n = int(input("Enter n:"))

    product = 1
    for i in range(2, n + 1):
        product *= i

    print(f"result: {product}")


def fibonacci():
    """fibonacci(n) = fibonacci(n-1) + fibonacci(n-2), e.g:
       1, 1, 2, 3, 5, 8, 13, 21...
    """
    n = int(input("Enter n:"))

    tail = 1
    head = 1

    # we can use _ because we don't care about the value of i
    for _ in range(n-2):
        head += tail
        tail = head - tail

    print(f"result: {head}")


def main():
    """entry point to the program
    """
    operations = {"qf": quadratic_formula, "!": factorial, "fib": fibonacci}

    print("Your options are:")
    print("\t- quadratic formula: qf")
    print("\t- factorial: !")
    print("\t- fibonacci: fib")
    choice = input("Enter your choice: ")

    operations[choice]()


if __name__ == "__main__":
    main()
