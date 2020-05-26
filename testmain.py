from tkinter import *
class Block:
    def __init__(self, x):
        self.e1 = Entry(x, width = 20)
        self.e2 = Entry(x, width = 20)
        self.b1 = Button(x, text = "+", bg='black', fg = "red", width = 16)
        self.b2 = Button(x, text = "-", bg='black', fg = "red", width = 16)
        self.b3 = Button(x, text = "*", bg='black', fg = "red", width = 16)
        self.b4 = Button(x, text = "/", bg='black', fg = "red", width = 16)
        self.l = Label(x, bg='black', fg='white', width=20)
        self.b1['command'] = self.funcs
        self.b2['command'] = self.funcm
        self.b3['command'] = self.funcmult
        self.b4['command'] = self.funcdiv
        self.e1.pack()
        self.e2.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.l.pack()
    def funcs(self):
        try:
            el1 = self.e1.get()
            el2 = self.e2.get()
            r = int(el1) + int(el2)
            self.l['text'] = str(r)
        except ValueError:
            self.l['text'] = 'Ошибка'
    def funcm(self):
        try:
            el1 = self.e1.get()
            el2 = self.e2.get()
            r = int(el1) - int(el2)
            self.l['text'] = str(r)
        except ValueError:
            self.l['text'] = 'Ошибка'
    def funcmult(self):
        try:
            el1 = self.e1.get()
            el2 = self.e2.get()
            r = int(el1) * int(el2)
            self.l['text'] = str(r)
        except ValueError:
            self.l['text'] = 'Ошибка'
    def funcdiv(self):
        try:
            el1 = self.e1.get()
            el2 = self.e2.get()
            r = int(el1) / int(el2)
            self.l['text'] = str(r)
        except ValueError:
            self.l['text'] = 'Ошибка'
root = Tk()
root.geometry('400x250')
root.title("Калькулятор")
block1 = Block(root)
root.mainloop()
