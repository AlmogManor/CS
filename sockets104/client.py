"""
Author: Almog Manor
Simple stdin -> socket client (with 4-bytes-length protocol)
"""
from socket import socket
from threading import Thread
from utils import send, receive, time_exit


EXIT_MESSAGE = "exit"


def make_client() -> socket:
    """creates a client and connects it

    Returns:
        socket: the connected socket
    """
    client = socket()
    client.connect(("127.0.0.1", 1324))
    return client


def main():
    """entry point to the program
    """
    time_stopper = Thread(target=time_exit)
    time_stopper.start()

    client = make_client()

    message = input("enter message to send: ")
    while message != EXIT_MESSAGE:
        send(client, message)
        print(f"server returned: {receive(client)}")

        message = input("Enter message to send:")

    send(client, EXIT_MESSAGE)
    client.close()


if __name__ == "__main__":
    main()
