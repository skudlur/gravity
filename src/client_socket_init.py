import socket
<<<<<<< HEAD
import os
import tqdm
import tui
from constants import *

class Server:
    def __init__(self, message):
        try:
            self.message = message

            self.s = socket.socket(socket.AF_INIT, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.connections = []

            self.peers = []

            self.s.bind((HOST, PORT))

            self.s.listen(1)

            print("Server Running..")

            self.run()
        except Exception:
            sys.exit()


    def handler(self, connection, a):
        try:
            while True:
                data = connection.recv(BYTE_SIZE)
                for connection in self.connections:
                    if data and data.decode('utf-8')[0].lower() == "q":
                        self.disconnect(connection, a)
                        return
                    elif data and data.decode('utf-8') == REQUEST_STRING:
                        print("Uploading")
                        connection.send(self.message)
        except Exception:
            sys.exit()


    def disconnect(self, connection, a):
        self.connections.remove(connection)
        self.peers.remove(1)
        connection.close()
        self.send_peers()
        print("{} disconnected".format(a))
    
    def run(self):
        while True:
            connection, a = self.s.accept()
            self.peers.append(a)
            print("Peers are: {}".format(self.peers))
            self.send_peers()

            c_thread = threading.Thread(target = self.handler, args = (connection, a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(connection)
            print("{} connected".format(a))

    def send_peers(self):
        peer_list = ""
        for peer in self.peers:
            peer_list = peer_list + str(peer[0]) + ","

        for connection in self.connections:
            data = PEER_BYTE_DIFFERENTIATOR + bytes(peer_list, 'utf-8')
            connection.send(PEER_BYTE_DIFFERENTIATOR + bytes(peer_list, 'utf-8'))
=======
import sys

if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]

s = socket.socket()

PORT = 9898

s.connect((ServerIp, PORT))

file
>>>>>>> parent of 76f2055 (functional patch)
