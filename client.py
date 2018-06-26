from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

HOST = '127.0.0.1'
PORT = 48423
RETRY_TIME = 5

if __name__ == '__main__':

    connected = False
    # Create Socket
    socket = socket(AF_INET, SOCK_STREAM)
    while (not connected):
        try:
            print("Attempting to connect to {}:{}".format(HOST, PORT))
            socket.connect((HOST, PORT))
            print("Connected...")
            connected = True
        except ConnectionRefusedError:
            print("Failed to connect. \nRetrying in {} seconds".format(RETRY_TIME))
            sleep(RETRY_TIME)
            
    while(True):
        message = b'o/'
        print("sending Message: {}".format(message))
        socket.sendall(b'o/')
        sleep(1)
