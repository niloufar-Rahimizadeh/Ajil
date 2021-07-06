from tkinter import *
from datetime import datetime

# #########functions###########


def get_date():
    dt = datetime.now()
    return dt.strftime('%d %b %Y')


def get_time():
    dt = datetime.now()
    return dt.strftime("%H:%M:%S")


def get_number():
    global counter, counter_list
    counter += 1
    counter_list.append(counter)
    con['date']['textvariable'].set(get_date())
    con['time']['textvariable'].set(get_time())
    con['number']['textvariable'].set("Your Turn {}".format(counter))
    con['waiting']['textvariable'].set("Waiting {}".format(len(counter_list)))


counter = 0
counter_list = []
root = Tk()
root.title('bank turning')
root.geometry('190x250')
root.configure(bg='#b7c4c0')

con = {
    'turn':{
        'text':'get a number',
        'width':10,
        'height':5,
        'bg':'#91ff59'
    },
    'cancel':{
        'text':'Cancel',
        'width':10,
        'height':5,
        'bg':'#eb8f34'
    },
    'op1':{
        'text': 'Operator1',
        'width': 10,
        'height':5,
        'bg':'#74b559'
    },
    'op2':{
        'text': 'Operator2',
        'width': 10,
        'height':5,
        'bg':'#74b559'
    },
    'op3':{
        'text': 'Operator3',
        'width': 10,
        'height':5,
        'bg':'#74b559'
    },
    'lop1': {
        'textvariable': StringVar(),
        'width': 10,
        'height':2,
        'bg':'#11bccf'
    },
    'lop2':{
        'textvariable': StringVar(),
        'width': 10,
        'height':2,
        'bg':'#11bccf'
    },
    'lop3':{
        'textvariable': StringVar(),
        'width': 10,
        'height':2,
        'bg': '#11bccf'
    },
    'number': {
        'textvariable': StringVar(),
    },
    'waiting': {
        'textvariable': StringVar(),

    },
    'time': {
        'textvariable': StringVar(),

    },
    'date': {
        'textvariable': StringVar(),

    }

}

Button(root, cnf=con['turn'], command=get_number).grid(row=0, column=0, padx=42, pady=5)
Button(root, cnf=con['cancel'], command=root.destroy).grid(row=1, column=0, padx=42, pady=10)
customers = Toplevel()
customers.title("Customers")
customers.geometry("200x200")
customers.configure(bg="#e8ebbc")
Label(customers, cnf=con['number']).grid(row=0, column=0, padx=45)
Label(customers, cnf=con['waiting']).grid(row=1, column=0, padx=45)
Label(customers, cnf=con['time']).grid(row=2, column=0, padx=45)
Label(customers, cnf=con['date']).grid(row=3, column=0, padx=45)

operators = Toplevel()
operators.title("Operators")
operators.geometry("600x200")
operators.configure(bg="#e0f5d7")

Button(operators, cnf=con['op1']).grid(row=0, column=0, padx=45, pady=25)
Button(operators, cnf=con['op2']).grid(row=0, column=1, padx=45, pady=25)
Button(operators, cnf=con['op3']).grid(row=0, column=2, padx=45, pady=25)

Label(operators, cnf=con['lop1']).grid(row=1, column=0, padx=45, pady=25)
Label(operators, cnf=con['lop2']).grid(row=1, column=1, padx=45, pady=25)
Label(operators, cnf=con['lop3']).grid(row=1, column=2, padx=45, pady=25)

root.mainloop()