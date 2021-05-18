from tkinter import *
from time import sleep

####################function###############

def start(v,o):
    while v:
        sleep(1)
        v -=1
        o.set(v)
        root.update()

##########################################
root = Tk()
l1 = Label(root, text="Time Input: ")
l1.grid(row=0, column=0)

var1 = StringVar()
e1 = Entry(root, textvariable=var1)
e1.grid(row=0, column=1)

var2 =StringVar()
var2.set("00")
l2 = Label(root, textvariable=var2)
l2.grid(row=1, column=0, columnspan=2)

b1 = Button(root, text="Start", 
command= lambda:start(int(var1.get()), var2))
b1.grid(row=2, column=0, columnspan=2, sticky='we')

root.mainloop()