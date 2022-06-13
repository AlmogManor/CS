"""
Author: Almog Manor
A script to demonstrate how to avoid race conditioning
"""
from sys import argv
from threading import Thread

# the bit of code in the beginning gets the folder that the .py file is save in
FILE = '\\'.join(argv[0].split('\\')[0:-1]) + "\\race_condition_fixed.txt"

IS_FILE_OPEN = False

def write_letter_by_letter(filename: str, text: str):
    """writes a string letter by letter to a given file

    Args:
        filename (str): the path to the file to write to
        text (str): the text to write
    """
    # declare it so we can edit the variable
    global IS_FILE_OPEN

    # we open with "a" for append, adding to the end of the file
    # opening with "w" will cause each letter to overwrite the previous one
    for letter in text:
        while IS_FILE_OPEN:
            pass

        IS_FILE_OPEN = True
        with open(filename, "a", encoding="ascii") as dest:
            dest.write(letter)
        IS_FILE_OPEN = False
        # because we are writing short text, to show you that the text won't always
        # be written in the correct order

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
