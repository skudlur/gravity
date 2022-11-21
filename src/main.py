import server_socket_init as ssi
import client_socket_init as csi
import os
import gravity_modules as gm

ip_list = []

while True:
    print("Modes available: \n1.Recieve\n2.Send")
    mode = int(input("Choose the mode(number):  "))

    if (mode == 1):
        ssi.socket_init()
        break
    elif (mode == 2):
        ip_list = gm.ip_list[1:-1]
        for i in range(len(ip_list)-1):
            print(f"{i}.{ip_list[i]}")
        ip_choose = input("Choose the IP to send the file to: ")
        if (ip_choose in ip_list):
            csi.host = ip_choose
        else:
            raise Exception("IP not found!")
        csi.filename = str(input("Enter your filename: "))
        csi.filesize = os.path.getsize(csi.filename)
        csi.socket_init()
        break
    elif (mode != 1 or mode != 2):
        raise Exception("Wrong mode")

