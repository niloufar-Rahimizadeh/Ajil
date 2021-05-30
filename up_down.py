from tkinter import *

def up():
    v = int(var1.get())
    v += 1
    var1.set(v)
    check()

def down():
    v = int(var1.get())
    v -= 1
    var1.set(v)
    check()

def check():
    v= int(var1.get())
    if v>0:
        l1.configure(bg="light green")
    else:
        l1.configure(bg='light blue')

root  = Tk()
Button(root, text="up", command=up).place(x=70, y=50)

var1 = StringVar()
var1.set("0")
l1 = Label(root, textvariable=var1)
l1.place(x=85, y=92)
Button(root, text="down", command=down).place(x=60, y=120)

root.mainloop()