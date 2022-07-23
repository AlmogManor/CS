"""
Author: Almog Manor
Multithreaded session based echo server
"""
from socket import socket
from threading import Thread
from utils import send, receive, keyboard_exit, time_exit


EXIT_MESSAGE = "exit"


def make_server() -> socket:
    """make a server socket

    Returns:
        socket: the created socket
    """
    server = socket()
    server.bind(("0.0.0.0", 1324))
    server.listen(5)
    return server


def launch_exit_mechanisms():
    """launch background threads that will cause the program to
       exit when enter is pressed or after 5 minutes
    """
    # exit after pressing enter, so the program can exit gracefully
    keyboard_stopper = Thread(target=keyboard_exit)
    keyboard_stopper.start()

    # because I know you will forget to close it, after 5
    # minutes the program will exit in its own
    time_stopper = Thread(target=time_exit)
    time_stopper.start()


def handle_client(client: socket):
    """handle echo server over 4-bytes-length protocol

    Args:
        client (socket): the client to communicate with
    """
    message = receive(client)

    while message != EXIT_MESSAGE:
        send(client, message)
        message = receive(client)

    client.close()


def main():
    """entry point to the program
    """
    launch_exit_mechanisms()
    server = make_server()

    # we can leave this as while True thanks to launch_exit_mechanisms()
    while True:
        client, address = server.accept()
        print(f"new client: {address}")

        client_thread = Thread(target=handle_client, args=[client])
        client_thread.start()


if __name__ == "__main__":
    main()
