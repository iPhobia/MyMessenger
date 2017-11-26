import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)
        print(data)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass



if __name__ == "__main__":

    HOST, PORT = "localhost", 14900
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    print("Server is running on address:", server.server_address)
    server.serve_forever()

        #https://docs.python.org/3/library/socketserver.html#module-socketserver
        #https://docs.python.org/3.6/library/threading.html#module-threading