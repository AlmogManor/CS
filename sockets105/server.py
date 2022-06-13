"""
Author: Almog Manor
Multithreaded session based echo server
"""
from socket import socket
from threading import Thread
from sys import argv
from utils import send_str, receive_str, keyboard_exit, time_exit, receive
from consts import EXIT, FILE, TEXT

# current working directory
CWD = '\\'.join(argv[0].split('\\')[0:-1]) + "\\"


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
    running = True
    message_type = receive_str(client)

    while running:
        if message_type == EXIT:
            running = False

        elif message_type == FILE:
            filename = CWD + receive_str(client)
            data = receive(client)
            with open(filename, "wb") as dest:
                dest.write(data)
                # make the computer write to the file now, without delay
                dest.flush()

        elif message_type == TEXT:
            message = receive_str(client)
            send_str(client, message)

        message_type = receive_str(client)

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
