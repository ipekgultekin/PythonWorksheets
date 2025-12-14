from tkinter import *
from tkinter import messagebox

class Fahrenheit(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Fahrenheit -> Celsius")
        self.pack()

        self.fahLabel = Label(self, text="Fahrenheit: ")
        self.fahLabel.pack(padx=5, pady=5, side=LEFT)

        self.msgEntry = Entry(self)
        self.msgEntry.pack(padx=5, pady=5, side=LEFT)

        self.button = Button(self, text="Convert it to Celsius", command=self.calculateCelsius)
        self.button.pack(padx=5, pady=5, side=LEFT)

    def calculateCelsius(self):
        value = float(self.msgEntry.get())
        result = float(5/9*(value-32))
        messagebox.showinfo("Celsius Equivalent", str(value) + " Fahrenheit = " + str(result) + " Celsius")

if __name__ == "__main__":
    f = Fahrenheit()
    f.mainloop()