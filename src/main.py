import server_socket_init as ssi
import client_socket_init as csi
import os

while True:
    print("Modes available: \n1.Recieve\n2.Send")
    mode = int(input("Choose the mode(number):  "))

    if (mode == 1):
        ssi.socket_init()
    elif (mode == 2):
        csi.filename = str(input("Enter your filename: "))
        csi.filesize = os.path.getsize(csi.filename)
        csi.socket_init()
    elif (mode != 1 or mode != 2):
        raise Exception("Wrong mode")
