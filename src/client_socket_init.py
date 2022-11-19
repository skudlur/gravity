import socket
import sys

if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]

s = socket.socket()

PORT = 9898

s.connect((ServerIp, PORT))

file
