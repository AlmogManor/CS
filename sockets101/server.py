"""
Author: Almog Manor

A simple module to explain the usage of TCP servers
"""
from socket import socket, AF_INET, SOCK_STREAM


def main():
    """
        This is the start of the program
    """

    # when we write: socket(AF_INET, SOCK_STREAM)
    # we mean:       socket(   IP  ,     TCP    )

    # other options:
    #   where we use AF_INET:
    #       AF_INET      - IPv4
    #       AF_INET6     - IPv6
    #       AF_BLUETOOTH - Bluetooth
    #
    #   where we user SOCK_STREAM:
    #       SOCK_DGRAM - UDP
    #
    #   keep in mind that the second parameter is dependant on the first one,
    #   for example, AF_BLUETOOTH may not support support SOCK_DGRAM

    # because the default is socket(AF_INET, SOCK_STREAM),
    # in later exercises we will just use:
    # server = socket()
    # this saves the imports and extra work
    server = socket(AF_INET, SOCK_STREAM)

    # the IP address given in bind is which addresses to accept,
    # e.g:
    # if we did server.bind(("8.8.8.8", 1324))
    # we would only be able to receive clients from 8.8.8.8 (Google's DNS server btw)
    # the PORT is the port to listen to, for ports below 1024 you need
    # to run your software with administrator privileges
    # because those ports are taken by the operating system
    server.bind(("0.0.0.0", 1324))

    # the amount of clients that can wait in queue before we accept their connection
    server.listen(5)

    # wait for a client to connect and accept a connection from the first one
    client, address = server.accept()

    # address is a tuple made out of (source IP, source PORT)
    print(f"client ip: {address[0]}, client port: {address[1]}")

    # read 1024 bytes from the socket, THIS IS NOT GUARANTEED
    # things can can cause recv() to return before 1024 bytes were received:
    #   EOF (end of file) was send
    #   timeout
    #   connection closed (TCP shutdown/reset was sent)
    message = client.recv(1024)

    # since python 3, data from recv() is returned as bytes and not as str,
    # so we have to convert it to str
    # why utf-8 and not ascii? utf-8 supports Hebrew if you want to use it
    message = message.decode("utf-8")

    # because this is an example we don't care if we actually read 1024 bytes
    # later on we will see how to properly write code to receive from a socket

    print(f"received from client: {repr(message)}")

    # terminate connection with the client, no more data will be sent or received
    client.close()

    # close the server, we can no longer accept clients, and the port is released
    server.close()


if __name__ == "__main__":
    main()
