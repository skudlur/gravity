import socket

s = socket.socket()

PORT = 9898
print("Server side initiated on port number:", PORT) 

s.bind(('', PORT))

s.listen(10)

file = open("../Documents/test.txt", "wb")
print("File staged to send to receiver")

while True:
    conn, addr = s.accept()

    conn.send(msg.encode())

    recvData = conn.recv(1024)
    while recvData:
        file.write(recvData)
        recvData = conv.recv(1024)

    file.close()
    print("Staged file sent successfully")

    conn.close()
    print("Server-client connection closed")

    break
