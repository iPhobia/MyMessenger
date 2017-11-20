import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 14900))
sock.listen(1)
conn, addr = sock.accept()
data = conn.recv(1024)
udata = data.decode("utf-8")
print("Data: " + udata)
conn.send(b"Hello\n")
conn.send(b"Your data: " + udata.encode("utf-8"))
conn.close()

