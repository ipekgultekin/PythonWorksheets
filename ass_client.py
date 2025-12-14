from socket import *
from tkinter import *
from tkinter import messagebox

class ClientScreen(Frame):
    def __init__(self, cSocket):
        Frame.__init__(self)
        self.cSocket = cSocket

        servermsg = self.cSocket.recv(1024).decode() #when I receive it i will decode it
        print(servermsg)

        self.master.title("Client Screen")
        self.pack()

        self.msgLabel = Label(self, text="Message: ")
        self.msgLabel.pack(padx=5, pady=5, side=LEFT)

        self.msgEntry = Entry(self)
        self.msgEntry.pack(padx=5, pady=5, side=LEFT)

        self.button = Button(self, text="Send", command= self.sendMessage)
        self.button.pack(padx=5, pady=5, side=LEFT)

    def sendMessage(self):
        clientmsg = "CLIENT>>" + self.msgEntry.get()
        self.cSocket.send(clientmsg.encode())
        if clientmsg == "CLIENT>>bye":
            self.cSocket.close()
            self.master.destroy()
        else:
            servermsg = self.cSocket.recv(1024).decode().replace("SERVER>>", "")
            messagebox.showinfo("Message", servermsg)


HOST = "127.0.0.1" #host address of server
PORT = 5000

socket = socket(AF_INET, SOCK_STREAM)
socket.connect((HOST, PORT))
window = ClientScreen(socket)
window.mainloop()