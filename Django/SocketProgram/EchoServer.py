import socket
import threading

class EchoServer:

    def __init__(self,addr,port = 5050,timeout = 7):
        self.addr = addr
        self.port = port
        self.timeout = timeout
        self.server_socket = None


    def __enter__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.addr,self.port))
        self.server_socket.settimeout(self.timeout)
        self.server_socket.listen(5)
        print(f"[LISTENING] at port: {self.port} at address: {self.addr}")
        return self

    # def __start__()

    def __exit__(self, exc_type, exc_value, traceback):
        if(exc_type is not None):
            print("Server Shuting down")


# with EchoServer(socket.gethostbyname(socket.gethostname()),5050) as server:
#     print("Test")

with EchoServer('742198794871',5050) as server:
    server.start()