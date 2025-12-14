from socket import *

HOST = "127.0.0.1"  # first one IP address
PORT = 5000  # second one port number


def loadDict(path="words.txt"):
    d = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            word, mean = line.split(";", 1)
            d[word.strip()] = mean.strip()
    return d


dic = loadDict()

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
print("Server started")
print("Waiting for connection requests")

while True:
    server.listen()
    clientsocket, clientaddress = server.accept()
    print("Connected: ", clientaddress)
    msg = "welcome".encode()
    clientsocket.send(msg)
    while True:
        data = clientsocket.recv(1024).decode()
        meaning = dic.get(data, "NOT FOUND")
        if meaning.lower() == "quit":
            break
        clientsocket.send(meaning.encode())

    clientsocket.close()