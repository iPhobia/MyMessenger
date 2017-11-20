import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 14900))
    sock.sendall(bytes('Hello AsyncServer', 'ascii'))
    response = str(sock.recv(1024), 'ascii')
    print("Received: {}".format(response))