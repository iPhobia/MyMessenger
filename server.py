import socket

with socket.socket() as sock:
    sock.bind(("", 14900))
    sock.listen(2)
    while True:
        conn, addr = sock.accept()
        print(f"User connected with address: {addr}")
        rawData = conn.recv(1024)
        data = rawData.decode("utf-8")
        print(f"Client sent: {data}")
        conn.send(data.encode())
        conn.close()



