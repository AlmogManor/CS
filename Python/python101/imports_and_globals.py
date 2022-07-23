"""
Author: Almog Manor
Demonstrate common import and global mistakes
"""
# import the entire file sys.py, just like copy and paste into out file
import sys
# import only the function sqrt from math.py
from math import sqrt
# import only the function log10 from math.py and rename it to log
from math import log10 as log
# import say_hello from bad_import_file
# because when we import, python runs the entire file we import,
# the garbage print inside bad_import_file.py will be called,
# which is why we use __name__ == "__main__"
from bad_import_file import say_hello
# this is a good import, it uses __name__ == "__main__"
# we have to import with "as" or we will have a name conflict
from good_import_file import say_hello as print_hello


GLOBAL_VAR = 3


def main():
    """entry point to the program
    """
    # if we want to write to GLOBAL_VAR, we need to declare it,
    # otherwise python will create a variable called GLOBAL_VAR
    # inside out function, just like a normal variable
    global GLOBAL_VAR
    GLOBAL_VAR = 8

    # we can use things from sys like this:
    print(f"sys.argv: {sys.argv}")

    # we can use sqrt() as if it was written in our file
    print(f"sqrt: {sqrt(5)}")

    # we can use log10 with the name log, log10 WON'T WORK
    print(f"log: {log(100)}")

    # we can user say_hello from bad_import_file
    print("bad file say hello:")
    say_hello()

    # we can user say_hello from good_import_file with the name print_hello
    print("good file say hello:")
    print_hello()


if __name__ == "__main__":
    main()

