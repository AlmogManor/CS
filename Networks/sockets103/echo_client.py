"""
Author: Almog Manor
Simple sockets client to send and receive a single message
"""
from socket import socket


def main():
    """the entry point to the program
    """
    client = socket()
    client.connect(("127.0.0.1", 1324))

    message = input("Enter a message:")
    client.sendall(message.encode("utf-8"))

    server_response = client.recv(4096).decode("utf-8")
    print(f"server said: {repr(server_response)}")


if __name__ == "__main__":
    main()
