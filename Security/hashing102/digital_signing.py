"""
Author: Almog Manor
A module to explain the concept of digital signing
"""
from hashlib import sha256
from sys import argv


# this returned the folder the .py is stored in (CWD = Current Working Directory)
CWD = '\\'.join(argv[0].split('\\')[0:-1]) + "\\"


def sign_file(filename:str) -> str:
    """sign a file with sha256

    Args:
        filename (bytes): the file to sign

    Returns:
        str: the signature, returned as a hex-string
    """
    with open(CWD + filename, "rb") as src:
        data = src.read()

    return sha256(data).hexdigest()


def create_and_write(filename:str, contents:str):
    """creates a file at CWD and writes to it

    Args:
        filename (str): the file to create
        contents (str): the data to write
    """
    with open(CWD + filename, "wb") as dest:
        dest.write(contents.encode("utf-8"))


def main():
    """entry point
    """
    create_and_write("file1", "This is some random text, the point here is that the text is extremely long but the signature stays the same size no matter what, so we can use this to verify the integrity of large file, like when we send them over the network, because even with TCP they have a change to get corrupted sometimes, or maybe a malicious hacker can interfere")
    #                                           |
    #                                           V
    create_and_write("file2", "This is some rand0m text, the point here is that the text is extremely long but the signature stays the same size no matter what, so we can use this to verify the integrity of large file, like when we send them over the network, because even with TCP they have a change to get corrupted sometimes, or maybe a malicious hacker can interfere")

    file1_signature = sign_file("file1")
    file2_signature = sign_file("file2")

    print(f"file1: {file1_signature}")
    print(f"file2: {file2_signature}")

    print(file1_signature == file2_signature)


if __name__ == "__main__":
    main()
