from tkinter import *

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Calculator")

        #it can be expanded (we need to specify it) büyütünce büyüsün diye ama sadece bu iki satırı yapınca calculator oynuyor sadece
        self.master.rowconfigure(0, weight=1) #weight=0 olursa not expandeable yani 0 dışında bi şey olmalı
        self.master.columnconfigure(0, weight=1)

        for i in range(0, 5):
            self.rowconfigure(i, weight=1)
        for j in range(0, 4):
            self.columnconfigure(j, weight=1)

        self.grid(sticky= W+E+N+S) #bu sefer grid structure kullanacağımız için grid dedik, normalde pack demiştik
        self.mainEntry = Entry(self, justify=RIGHT) #put everything in this window, calculator'de text sağda olur diye right dedik
        self.mainEntry.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
        #entry block'unu 4 columns'a genişletmek istediğim için sondaki şeyi yazdık
        #sticky: bir positiona koyduktan sonra etrafında boşluklar olur, genişletince (resize) all direction'a uysun diye koyuyoruz

        items = [["7", "8", "9", "/"], ["4", "5", "6", "*"], ["1", "2", "3", "-"], ["0", ".", "=", "+"]] #aynı line'dakileri sublist olarak ekledik
        for i in range(0,4):
            for j in range(0,4):
                if items[i][j] == "=":
                    self.button = Button(self, text=items[i][j], command=self.calculate) #command: if = clicked, calculate result and put it entry box (self.calculate function will be executing)
                else:
                    self.button = Button(self, text=items[i][j]) #only specify its text without command!
                    self.button.bind("<Button-1>", self.buttonPressed)# bind a specific method, self.buttonPressed: differentiated which one is clicked
                    #button1 : left click of mouse, button2 : right click of mouse
                self.button.grid(row=i+1, column=j, sticky=W+E+N+S) #entry box: index 0 o yüzden +1 dedik ama column'da directly use j

    def calculate(self):
        value = self.mainEntry.get() #what we have inside of it
        result = eval(value) #eval dangerous'tu ama yine de kullandık ??
        self.mainEntry.delete(0, END) #başta entry box'un içini temizledik
        self.mainEntry.insert(0, result) #entry box'a sonucu yerleştirdik

    def buttonPressed(self, event):
        #everything is a widget (entry box, buttons, checkbuttons, etc.)
        value = event.widget["text"] #herhangi birine bastığımızda event gerçekleşecek for this particular widget, and I take its text
        self.mainEntry.insert(END, value) #value added to the end instead of beginning

if __name__ == '__main__':
    c = Calculator()
    c.mainloop()


