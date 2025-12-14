from socket import *
from threading import *
import math

class ClientThread(Thread):

    def __init__(self, clientsocket, clientaddress):
        Thread.__init__(self)
        self.clientsocket = clientsocket
        self.clientaddress = clientaddress
        print("Connection from ", clientaddress)

    def run(self):
        msg = "welcome".encode()
        self.clientsocket.send(msg)

        while True:
            data = self.clientsocket.recv(1024).decode().strip()

            if data == "bye":
                break

            # Expected: What is sin(10)?
            answer = self.handle_question(data)
            self.clientsocket.send(answer.encode())

        self.clientsocket.close()

    def handle_question(self, q):
        # Very similar “simple parsing” approach, but stable & readable.
        # Returns a string (no bytes).

        q = q.strip()

        if not q.lower().startswith("what is "):
            return "ERROR: Use format -> What is func(value)?"

        # remove "What is "
        expr = q[8:].strip()  # after "What is "
        if expr.endswith("?"):
            expr = expr[:-1].strip()

        # expr should be like: sin(10)
        if "(" not in expr or not expr.endswith(")"):
            return "ERROR: Use format -> What is func(value)?"

        func_name = expr[:expr.index("(")].strip()
        value_str = expr[expr.index("(") + 1:-1].strip()

        # parse number
        try:
            value = float(value_str)
        except:
            return "ERROR: value must be a number"

        # supported functions
        try:
            if func_name == "sin":
                res = math.sin(value)
            elif func_name == "cos":
                res = math.cos(value)
            elif func_name == "tan":
                res = math.tan(value)
            elif func_name == "sqrt":
                if value < 0:
                    return "ERROR: sqrt needs non-negative value"
                res = math.sqrt(value)
            else:
                return "ERROR: Unknown function (sin/cos/tan/sqrt)"
        except Exception as e:
            return f"ERROR: {e}"

        return str(res)


HOST = "127.0.0.1"
PORT = 5000

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind((HOST, PORT))

print("Server started!")
print("Waiting for connection requests")

while True:
    server.listen()
    clientsocket, clientaddress = server.accept()
    newThread = ClientThread(clientsocket, clientaddress)
    newThread.start()
