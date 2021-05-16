import tkinter as tk 


root = tk.Tk()
root.geometry("200x200")
name = tk.StringVar()
name.set("Amir")
l1 = tk.Label(root, textvariable=name)
l1.grid(row=0, column=0)



##################
root.mainloop()