"""
Author: Almog Manor
A script made to demonstrate the basics of multithreading in python
"""
from threading import Thread
from time import time


def say_something(something: str, duration: int):
    """print something to the stdout for a given period of time

    Args:
        something (str): the text to print
        duration (int): the duration to print for (in seconds)
    """
    end_time = time() + duration
    while time() < end_time:
        print(something)


def main():
    """This is where the program starts
    """
    # here we create a thread object
    # threads have to be created and then started
    #
    # the target parameter is a POINTER to the function to run
    # don't forget: it is a POINTER, DO NOT add () after the function name
    #
    # the args parameter is a LIST of arguments to pass to the function
    # don't forget: it is a LIST, you NEED the [], even for one parameter
    thread1 = Thread(target=say_something, args=["Hello!", 5])
    thread2 = Thread(target=say_something, args=["Shalom!", 5])

    # here we start the thread, the main function continues to run
    # without waiting for the function in thread1 to finish
    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()
