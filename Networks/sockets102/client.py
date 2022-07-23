"""
Author: Almog Manor
A script demonstrating the use of the send function in utils.py
"""
from socket import socket
from utils import protocol_send


def main():
    """The program starts here
    """
    client = socket()
    client.connect(("127.0.0.1", 1324))

    protocol_send(client, "Hello")
    print("Sent!")


if __name__ == "__main__":
    main()
