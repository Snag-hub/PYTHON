# Write Python GUI program to accept a number n and check whether it is Prime,Perfect or Armstrong number or not. Specify three radio buttons.

import tkinter as tk
from tkinter import *
from tkinter import messagebox


def typeofnumber():
    value = entry.get()
    value = value.strip()
    select = radiovar.get()
    print(select)
    if (value.isdigit() and len(value) <= 3 and value != '0'):
        if select == 1:
            numbercheck = checkprime(value)
            messagebox.showinfo("Prime", numbercheck)
        elif select == 2:
            numbercheck = checkarmstrong(value)
            messagebox.showinfo("Armstrong", numbercheck)
        elif select == 3:
            numbercheck = checkperfect(value)
            messagebox.showinfo("Perfect", numbercheck)
        else:
            messagebox.showinfo("Number", "A Number")
    else:
        messagebox.showerror(
            "Number Error", "Number Error Something went wrong!")


def checkprime(no):
    print("Check Prime called" + no)
    no = int(no)
    if no > 1:
        for i in range(2, no):
            if (no % i) == 0:
                return "Number is not a Prime No"
            else:
                return "Number is Prime No"
    else:
        return "Number is not a Prime No"


def checkarmstrong(no):
    # initialize sum
    sum = 0
    no = int(no)

    # find the sum of the cube of each digit
    temp = no
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10

    # display the result
    if no == sum:
        print(no, "is an Armstrong number")
        return "Number is a Armstrong number"
    else:
        print(no, "is not an Armstrong number")
        return "Number is a not Armstrong number"


def checkperfect(no):
    i = 2
    sum = 1
    no = int(no)
    while (i <= (no // 2)):
        if (no % i == 0):
            sum += i
        i += 1

    if sum == no:
        print(no, "is a perfect number")
        return "Number is a perfect number"
    else:
        print(no, "is not a perfect number")
        return "Number is not a perfect number"


window = Tk()
window.geometry('800x400')
window.title('Slip 9b')
intvar = IntVar()
radiovar = IntVar()
label = Label(text='Enter Number')
entry = Entry(window, textvariable=intvar)
radiobuttonprime = Radiobutton(
    window, text='Prime', variable=radiovar, value=1, command=typeofnumber)
radiobuttonprime.place(anchor='e')
radiobuttonarmstrong = Radiobutton(
    window, text='Armstrong', variable=radiovar, value=2, command=typeofnumber)
radiobuttonarmstrong.place(anchor='w')
radiobuttonperfect = Radiobutton(
    window, text='Perfect', variable=radiovar, value=3, command=typeofnumber)
radiobuttonperfect.place(anchor='center')
label.grid(row=1, column=1)
entry.grid(row=1, column=2)
radiobuttonprime.grid(row=2, column=1)
radiobuttonarmstrong.grid(row=2, column=2)
radiobuttonperfect.grid(row=2, column=3)
window.pack_slaves()
window.mainloop()
