from tkinter import *
window = Tk()
window.geometry("1080x720")
ent = Entry(window, width=60,)
ent.place(x=10, y=10)
def click(num):
    result = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(result) + str(num))
b = Button(window, text = '1', width = 10, height = 1, command = lambda:click(1))
b.place(x=10, y=50)
b = Button(window, text = '2', width = 10, height = 1, command = lambda:click(2))
b.place(x=100, y=50)
b = Button(window, text = '3', width = 10, height = 1, command = lambda:click(3))
b.place(x=190, y=50)
b = Button(window, text = '4', width = 10, height = 1, command = lambda:click(4))
b.place(x=10, y=90)
b = Button(window, text = '5', width = 10, height = 1, command = lambda:click(5))
b.place(x=100, y=90)
b = Button(window, text = '6', width = 10, height = 1, command = lambda:click(6))
b.place(x=190, y=90)
b = Button(window, text = '7', width = 10, height = 1, command = lambda:click(7))
b.place(x=10, y=130)
b = Button(window, text = '8', width = 10, height = 1, command = lambda:click(8))
b.place(x=100, y=130)
b = Button(window, text = '9', width = 10, height = 1, command = lambda:click(9))
b.place(x=190, y=130)
b = Button(window, text = '0', width = 10, height = 1, command = lambda:click(0))
b.place(x=100, y=170)
def multiply():
    n1 = ent.get()
    global math
    math = 'Multiplication'
    global i
    i = int(n1)
    ent.delete(0, END)
b = Button(window, text = '*', width = 10, height = 1, command = multiply)
b.place(x=10, y=170)
def divide():
    n1 = ent.get()
    global math
    math = 'Division'
    global i
    i = int(n1)
    ent.delete(0, END)
b = Button(window, text = '/', width = 10, height = 1, command = divide)
b.place(x=280, y=50)
def add():
    n1 = ent.get()
    global math
    math = 'Addition'
    global i
    i = int(n1)
    ent.delete(0, END)
b = Button(window, text = '+', width = 10, height = 1, command = add)
b.place(x=280, y=90)
def sub():
    n1 = ent.get()
    global math
    math = 'Subtraction'
    global i
    i = int(n1)
    ent.delete(0, END)
b = Button(window, text = '-', width = 10, height = 1, command = sub)
b.place(x=280, y=130)
def equal():
    n2 = ent.get()
    ent.delete(0, END)
    if math == 'Multiplication':
        ent.insert(0, i * int(n2))
    elif math == 'Division':
        ent.insert(0, i / int(n2))
    elif math == 'Addition':
        ent.insert(0, i + int(n2))
    elif math == 'Subtraction':
        ent.insert(0, i - int(n2))

b = Button(window, text = '=', width = 10, height = 1, command = equal)
b.place(x=190, y=170)
def clear():
    ent.delete(0, END)
b = Button(window, text = 'Clear', width = 10, height = 1, command = clear)
b.place(x=280, y=170)

window.mainloop()