# Write Python GUI program to accept a decimal number and convert and display it to binary, octal and hexadecimal number.

from tkinter import *


def convert():
    # get the value from the entry box
    num = int(e.get())
    # convert the number to binary
    binary = bin(num)
    # convert the number to octal
    octal = oct(num)
    # convert the number to hexadecimal
    hexadecimal = hex(num)
    # display the result
    lbl.configure(text="Binary: " + binary + "\nOctal: " +
                  octal + "\nHexadecimal: " + hexadecimal)


window = Tk()
window.title("Convert")
window.geometry("300x200")
lbl = Label(window, text="Binary: \nOctal: \nHexadecimal: ")
lbl.grid(column=1, row=4)
e = Entry(window, width=10)
e.grid(column=1, row=1)
btn = Button(window, text="Convert", command=convert)
btn.grid(column=1, row=2)
window.mainloop()
