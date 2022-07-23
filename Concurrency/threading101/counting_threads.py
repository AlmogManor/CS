"""
Author: Almog Manor
A script that counts multithreaded
"""
from threading import Thread


def count(starting_point: int):
    """count 100 from a given number

    Args:
        starting_point (int): the number to start from
    """
    starting_point += 1
    for number in range(starting_point, starting_point + 100):
        print(number)


def main():
    """the starting point of the program
    """
    thread1 = Thread(target=count, args=[17])
    thread2 = Thread(target=count, args=[68])

    thread1.start()
    thread2.start()

    # wait for the threads to finish printing before we exit the program,
    # or else they will be killed before they get a chance to finish
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
