"""
Author: Almog Manor
Demonstrate how to use sha256 in python
"""
from hashlib import sha256


def main():
    """entry point to the program
    """

    message = "Hello, how are you doing?"
    message_bytes = message.encode("utf-8")

    # we can also use .digest() to get it as bytes and not hex-string
    hashed = sha256(message_bytes).hexdigest()
    print(hashed)


if __name__ == "__main__":
    main()
