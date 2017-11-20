import socket

with socket.socket() as conn:
    conn.connect(("127.0.0.1", 14900))
    conn.send(b"Hola")
    rawData = conn.recv(1024)
    data = rawData.decode("utf-8")
    print(f"From server: {data}")
    conn.close()