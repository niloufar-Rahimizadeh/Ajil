import tkinter as tk
from tkinter.constants import COMMAND

def up():
    l1.config(text=l1['text'] + 1)




def down():
    l1.config(text=l1['text'] - 1)




root = tk.Tk()
root.geometry('200x200')

l1 = tk.Label(root, text=0, font=('timse', 13))

l1.grid(row=1, column=0)

l3 = tk.Label(root, text='fan',font=('timse', 13))
l3.grid(row=1, column=2)

tk.Button(root, text='↑', font=('timse', 13), command=up).grid(row=0, column=0)

tk.Button(root, text='↓', font=('timse', 13), command=down).grid(row=2, column=0)

root.mainloop()