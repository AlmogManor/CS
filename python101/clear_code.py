"""
Author: Almog Manor
Demonstrate the usage of better coding practices in python, like f-strings
"""

def add(number1:int, number2:int) -> int:
    """Add two numbers together

    Args:
        number1 (int): the first number
        number2 (int): the seconds number

    Returns:
        int: their sum
    """
    return number1 + number2


def main():
    """entry point to the program
    """
    x = add(4, 8)
    # this is like doing "sum :" + str(x)
    print(f"sum: {x}")

    # this is like doing "sum :" + str(add(4, 8))
    sum_str = f"sum: {add(4, 8)}"
    print(sum_str)

    # this will print sum_str surrounded by ""
    print(repr(sum_str))


if __name__ == "__main__":
    main()
