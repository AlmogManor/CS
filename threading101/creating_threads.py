"""
Author: Almog Manor

"""
from threading import Thread
from time import time


RUNNING_TIME = 5 # in seconds


def say_hello():
    end_time = time() + RUNNING_TIME
    while time() < end_time:
        print("Hello!")


def say_shalom():
    end_time = time() + RUNNING_TIME
    while time() < end_time:
        print("Shalom!")


def main():
    thread1 = Thread(target=say_hello)
    thread2 = Thread(target=say_shalom)

    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()
