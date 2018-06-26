"""Example from python3 docs - All credit to them :)"""
from socket import socket, AF_INET, SOCK_STREAM
import sys

HOST = '127.0.0.1'
PORT = 48423
RECV_BYTES = 1024

if __name__ == '__main__':

    with socket(AF_INET, SOCK_STREAM) as my_sock:
        # Bind Socket to Host on Port
        my_sock.bind((HOST, PORT))
        my_sock.listen(1)
        connection, address = my_sock.accept()
        print("Waiting on Connection...")
        with connection:
            print("Connected to {}".format(address))
            while True:
                data = connection.recv(RECV_BYTES)
                if data: 
                    print("Message Recieved: {}".format(data))