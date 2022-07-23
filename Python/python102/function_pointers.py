"""
Author: Almog Manor
Example usage of function pointers
"""


def say_hello():
    print("hello")


def say_hi():
    print("hi")


def add_1(x:int) -> int:
    return x + 1


def add_3(x:int) -> int:
    return x + 3


def add_4(x:int) -> int:
    return x + 4


def main():
    function_list = [say_hello, say_hi]
    
    # this will call say_hello()
    function_list[0]()
    # this will call say_hi()
    function_list[1]()

    function_list = [add_1, add_3, add_4]

    print(function_list[0](1200))
    print(function_list[1](1200))
    print(function_list[2](1200))


if __name__ == "__main__":
    main()
