"""
Author: Almog Manor
Demonstrate what happens when you use __name__ == "__main__"
"""


def say_hello():
    """print hello!
    """
    print("hello!")


if __name__ == "__main__":
    print("this is leftover garbage")
