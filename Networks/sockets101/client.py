"""
Author: Almog Manor
A simple socket client
"""
from socket import socket


def main():
    """
        This is the starting point of the program
    """
    # remember that the default is socket(AF_INET, SOCK_STREAM)
    # meaning that we can leave it empty
    client = socket()

    # here we tell the socket the IP and the PORT to connect to
    client.connect(("127.0.0.1", 1324))

    # this is the same af writing:
    # "Hello!".encode("utf-8")
    # but faster. Notice the b before the ""
    message = b"Hello!"

    # .send() DOESN'T GUARANTEE that the entire message will be sent,
    # it returns the amount of bytes actually sent
    # if you want to guarantee that everything will be sent, use .sendall()
    # you should use .sendall() from now on almost always
    # why does .send() exists? A question for another day
    bytes_sent = client.sendall(message)
    print(f"sent {bytes_sent} bytes")


if __name__ == "__main__":
    main()
