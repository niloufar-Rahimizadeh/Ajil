from tkinter import *
from time import sleep

####################function###############

tick = True

def start(v, o):
    global tick
    tick = True
    while v:
        if not tick:
            return
        sleep(1)
        v -=1
        o.set(v)
        root.update()


def stop():
    global tick
    tick = False
    var1.set(var2.get())

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

b1 = Button(root, text="Stop", 
command= stop)
b1.grid(row=3, column=0, columnspan=2, sticky='we')

root.mainloop()