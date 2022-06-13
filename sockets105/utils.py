"""
Author: Almog Manor
Utility functions
"""
from socket import socket
from time import time, sleep
from os import _exit as force_exit


LENGTH_FIELD_SIZE = 4


def send(connection: socket, data: bytes):
    """send bytes with 4 bytes of length before

    Args:
        connection (socket): the socket to send the data through
        data (bytes): the data to send
    """
    length_bytes = int.to_bytes(len(data), LENGTH_FIELD_SIZE, byteorder="big")

    data_to_send = length_bytes + data

    connection.sendall(data_to_send)


def send_str(connection: socket, data: str):
    """send a str with 4 bytes of length before

    Args:
        connection (socket): the socket to send the data through
        data (str): the data to send
    """
    send(connection, data.encode("utf-8"))


def receive(connection: socket) -> bytes:
    """receive bytes with 4 byte of length before

    Args:
        connection (socket): the socket to read from

    Returns:
        bytes: the bytes read from the socket
    """
    # make sure that we actually read LENGTH_FIELD_SIZE bytes
    length_bytes = connection.recv(LENGTH_FIELD_SIZE)
    while len(length_bytes) != LENGTH_FIELD_SIZE:
        length_bytes += connection.recv(LENGTH_FIELD_SIZE - len(length_bytes))

    length = int.from_bytes(length_bytes, byteorder="big")

    data = b""
    while len(data) != length:
        data += connection.recv(length - len(data))

    return data


def receive_str(connection: socket) -> str:
    """receive a str with 4 byte of length before

    Args:
        connection (socket): the socket to read from

    Returns:
        str: the str read from the socket
    """
    return receive(connection).decode("utf-8")


def time_exit(wait: int = 300):
    """exit after a given amount of time

    Args:
        wait (int, optional): the number of seconds to wait. Defaults to 300.
    """
    exit_time = time() + wait
    while time() < exit_time:
        sleep(1)
    force_exit(0)


def keyboard_exit():
    """exit when enter is pressed
    """
    input("Press enter to exit\n")
    force_exit(0)
