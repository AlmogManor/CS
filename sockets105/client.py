"""
Author: Almog Manor
Simple client (with 4-bytes-length protocol), supports sending of files and text
"""
from socket import socket
from threading import Thread
from utils import send_str, receive_str, time_exit, send
from consts import EXIT, FILE, TEXT


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

    running = True

    message_type = input("enter message type (exit/file/text): ")
    while running:
        send_str(client, message_type)
        if message_type == EXIT:
            running = False

        elif message_type == FILE:
            path = input("Enter path to file (use \\ and not /): ")
            # get the name, not the entire path
            filename = path.split("\\")[-1]

            with open(path, "rb") as src:
                data = src.read()

            send_str(client, filename)
            send(client, data)

        elif message_type == TEXT:
            message = input("Enter message to send:")
            send_str(client, message)
            print(f"server returned: {receive_str(client)}")

        message_type = input("enter message type (exit/file/text): ")

    client.close()


if __name__ == "__main__":
    main()
