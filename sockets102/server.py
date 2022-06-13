"""
Author: Almog Manor
A simple script demonstrating the usage of the receive function in utils.py
"""
from socket import socket
from utils import protocol_receive


def main():
    """The starting point of the program
    """
    server = socket()
    server.bind(("0.0.0.0", 1324))
    server.listen(5)

    # we use _ here because we don't care about the address, we can discard the value
    client, _ = server.accept()

    message = protocol_receive(client)

    print(f"received: {repr(message)}")


if __name__ == "__main__":
    main()
