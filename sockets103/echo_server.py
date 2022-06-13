"""
Author: Almog Manor
Echo Server
"""
from socket import socket
from threading import Thread
from time import time, sleep
from os import _exit as force_exit


def keyboard_exit():
    """exit when enter is pressed
    """
    input("Press enter to exit\n")
    force_exit(0)


def time_exit(wait: int = 300):
    """exit after a given amount of time

    Args:
        wait (int, optional): the number of seconds to wait. Defaults to 300.
    """
    exit_time = time() + wait
    while time() < exit_time:
        sleep(1)
    force_exit(0)


def main():
    """the entry point to the program
    """
    # remember, the default is IP/TCP
    server = socket()
    server.bind(("0.0.0.0", 1324))
    server.listen(5)

    # exit after pressing enter, so the program can exit gracefully
    keyboard_stopper = Thread(target=keyboard_exit)
    keyboard_stopper.start()

    # because I know you will forget to close it, after 5 minutes the program
    # will exit in its own
    time_stopper = Thread(target=time_exit)
    time_stopper.start()

    while True:
        client, address = server.accept()
        print(f"accepted connection from: {address}")

        # we don't need encode() and decode() here because we don't need to parse the message
        message = client.recv(4096)
        client.sendall(message)

        client.close()


if __name__ == "__main__":
    main()
