"""
Author: Almog Manor
Utility functions to read and write to sockets with 4 bytes of length as header
"""
from socket import socket

LENGTH_FIELD_SIZE = 4


def protocol_send(connection: socket, data: str):
    """send a str with 4 bytes of length before

    Args:
        connection (socket): the socket to send the data through
        data (str): the data to send
    """
    data = data.encode("utf-8")
    length_bytes = int.to_bytes(len(data), LENGTH_FIELD_SIZE, byteorder="big")

    data_to_send = length_bytes + data

    connection.sendall(data_to_send)


def protocol_receive(connection: socket) -> str:
    """receive a str with 4 byte of length before

    Args:
        connection (socket): the socket to read from

    Returns:
        str: the str read from the socket
    """
    # make sure that we actually read LENGTH_FIELD_SIZE bytes
    length_bytes = connection.recv(LENGTH_FIELD_SIZE)
    while len(length_bytes) != LENGTH_FIELD_SIZE:
        length_bytes += connection.recv(LENGTH_FIELD_SIZE - len(length_bytes))

    length = int.from_bytes(length_bytes, byteorder="big")

    data = b""
    while len(data) != length:
        data += connection.recv(length - len(data))

    return data.decode("utf-8")
