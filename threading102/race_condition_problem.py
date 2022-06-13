"""
Author: Almog Manor
A script to demonstrate race conditioning
"""
from sys import argv
from threading import Thread

# the bit of code in the beginning gets the folder that the .py file is save in
FILE = '\\'.join(argv[0].split('\\')[0:-1]) + "\\race_condition.txt"


def write_letter_by_letter(filename: str, text: str):
    """writes a string letter by letter to a given file

    Args:
        filename (str): the path to the file to write to
        text (str): the text to write
    """
    # we open with "a" for append, adding to the end of the file
    # opening with "w" will cause each letter to overwrite the previous one
    for letter in text:
        with open(filename, "a", encoding="ascii") as dest:
            dest.write(letter)


def main():
    """this is the entry point to the program
    """
    with open(FILE, "w", encoding="ascii") as dest:
        dest.write("")

    thread1 = Thread(target=write_letter_by_letter, args=[FILE, "0123456789"])
    thread2 = Thread(target=write_letter_by_letter, args=[FILE, "abcdefghij"])

    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()

