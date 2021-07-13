import tkinter as tk
from tkinter import messagebox
# function

def press():
    messagebox.showinfo("show info", "Your information successfully is submitted")
    messagebox.showerror("Error", "")

root=tk.Tk()
root.geometry('280x350')
root.configure(bg='purple')
root.title('information')
root.resizable(0, 0)

app=tk.Tk()
app.geometry('180x100')
app.configure(bg='#ff8286')
app.resizable(1,1)

l1 = tk.Label(root, text='Name', bg='purple', fg='white', width=5, font=('timse',13))
l1.grid(row=0, column=0, padx=5, pady=5)

var1=tk.StringVar()
e1=tk.Entry(root, textvariable=var1)
e1.grid(row=0, column=1)


l2 = tk.Label(root, text='Age', bg='purple', fg='white', width=5, font=('times',13))
l2.grid(row=1, column=0, padx=5, pady=5)

s1=tk.Spinbox(root, from_=20, to=30, state='readonly', wrap=True)
s1.grid(row=1, column=1)

b1=tk.Button(app, text='Hide', bg='#c9067e', font=('times',11), command=root.withdraw)
b1.grid(row=2, column=0, padx=10, pady=10)


b2=tk.Button(app, text='Show', bg='#c9067e', font=('times',11), command=root.deiconify)
b2.grid(row=2, column=1, padx=10, pady=10)


l3 = tk.Label(root, text='Gender', bg='purple', fg='white', font=('times',13))
l3.grid(row=3, column=0, padx=5, pady=5)

var2 = tk.IntVar()
r1 = tk.Radiobutton(root, text='Male', variable=var2, value=1).grid(row=3, column=1)
r2 = tk.Radiobutton(root, text='Female', variable=var2, value=2).grid(row=4, column=1)
l4 = tk.Label(root, text='Language', bg='purple', fg='white', font=('times',13))
l4.grid(row=5, column=0, padx=5, pady=5)
var_cb1 = tk.StringVar()
tk.Checkbutton(root, text="English", variable=var_cb1, onvalue="English").grid(row=6, column=1)
var_cb2 = tk.StringVar()
tk.Checkbutton(root, text="Persian", variable=var_cb2, onvalue="Persian").grid(row=7, column=1)
var_cb3 = tk.StringVar()
tk.Checkbutton(root, text="German", variable=var_cb3, onvalue="German").grid(row=8, column=1)
tk.Button(root, text="submit",  bg='#c9067e', font=('times', 11), command=press).grid(row=9, column=1, pady=10)


root.mainloop()