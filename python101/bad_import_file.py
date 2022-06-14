"""
Author: Almog Manor
Demonstrate what happens when you don't use __name__ == "__main__"
"""


def say_hello():
    """print hello
    """
    print("hello")


print("this is leftover garbage")
