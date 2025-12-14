from socket import *
from threading import *

class ClientThread(Thread):
    def __init__(self, cSocket, cAddress):
        Thread.__init__(self)
        self.cSocket = cSocket
        self.cAddress = cAddress
        print("Connection successful from ", self.cAddress)

    def run(self):
        servermsg = "SERVER>>welcome".encode()
        self.cSocket.send(servermsg)
        clientmsg = self.cSocket.recv(1024).decode()
        while clientmsg != "CLIENT>>bye":
            servermsg = clientmsg.replace("CLIENT>>", "")
            servermsg = "SERVER>>" + servermsg
            self.cSocket.send(servermsg.encode())
            clientmsg = self.cSocket.recv(1024).decode()
        print("Connection closed from ", self.cAddress)
        self.cSocket.close()


HOST = "127.0.0.1"
PORT = 5000
socket = socket(AF_INET, SOCK_STREAM) #TCP kullandığımız için sock_stream kullanıyoruz UPD olsaydı başka bişey olurdu
socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #sol_socket this socket
socket.bind((HOST, PORT))

while True:
    socket.listen()
    cSocket, cAddress = socket.accept() # accept 2 thing: client socket, client address
    newClient = ClientThread(cSocket, cAddress)
    newClient.start()
