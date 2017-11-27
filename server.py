import socket
import _thread

connectedUsers = []
conn = socket.socket()
conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
conn.bind(('localhost',14900))

conn.listen(2)

def clientHandle(socc):
    while True:
        receivedData = socc.recv(1024).decode()
        print(receivedData)
        if receivedData:
            for users in connectedUsers:
                users.send("User ".encode()+receivedData.encode())
        if not receivedData:
            break

while True:
    socc, addr = conn.accept()
    connectedUsers.append(socc)
    _thread.start_new(clientHandle,(socc,))
    print("thread "+str(_thread.get_ident()))