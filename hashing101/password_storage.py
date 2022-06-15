"""
Author: Almog Manor
Demonstrate the usage of hashing to securely store sensitive data
"""
from hashlib import sha256


# why is this an independent function? It's just one line of code.
# the idea behind functions sometimes is to provide abstraction, this
# way, we can easily change the hashing algorithm used throughout the entire
# program, by changing just one place
def hash_str(text:str) -> str:
    """generate the sha256 hash of a given string

    Args:
        text (str): the string to hash

    Returns:
        str: the hash, returned as a hex-string
    """
    return sha256(text.encode("utf-8")).hexdigest()


def main():
    """entry point
    """
    password_raw = "P@$$w0rd"
    password_hash = hash_str(password_raw)

    input_password = input("Enter password: ")
    input_password_hash = hash_str(input_password)

    if password_hash == input_password_hash:
        print("correct password!")
    else:
        print("incorrect password :(")


if __name__ == "__main__":
    main()
