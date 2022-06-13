"""
Author: Almog Manor
A script made to demonstrate the basics of multithreading in python
"""
from threading import Thread
from time import time


RUNNING_TIME = 5  # in seconds


def say_hello():
    """prints Hello! for RUNNING_TIME seconds
    """
    end_time = time() + RUNNING_TIME
    while time() < end_time:
        print("Hello!")


def say_shalom():
    """prints Shalom! for RUNNING_TIME seconds
    """
    end_time = time() + RUNNING_TIME
    while time() < end_time:
        print("Shalom!")


def main():
    """This is where the program starts
    """
    # here we create a thread object
    # threads have to be created and then started
    # the target parameter is a POINTER to the function to run
    # don't forget: it is a POINTER, DO NOT add () after the function name
    thread1 = Thread(target=say_hello)
    thread2 = Thread(target=say_shalom)

    # here we start the thread, the main function continues to run
    # without waiting for the function in thread1 to finish
    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()
