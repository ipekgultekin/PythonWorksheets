from socket import *

HOST = "127.0.0.1"  # first one IP address
PORT = 5000  # second one port number

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    in_data = client.recv(1024).decode()
    print("Message from the server ", in_data)
    out_data = input("Enter word: ")
    client.send(out_data.encode())
    if out_data == "quit":
        break
client.close()