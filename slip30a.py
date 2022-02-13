# Write a Python GUI program to accept a string and a character from user and count the occurrences of a character in a string.

from tkinter import *



def Calculate():
    # get the value from the entry box
    string = e1.get()
    char = e2.get()
    # calculate the volume
    count = string.count(char)
    # display the result
    lbl.configure(text="The number of occurrences of " +
                  char + " in " + string + " is " + str(count))


window = Tk()
window.title("Count the number of occurrences of a character in a string")
window.geometry("300x200")
lbl = Label(window, text="The number of occurrences of ")
lbl.grid(column=1, row=4)
e1 = Entry(window, width=10)
e1.grid(column=1, row=1)
e2 = Entry(window, width=10)
e2.grid(column=1, row=2)
btn = Button(window, text="Calculate", command=Calculate)
btn.grid(column=1, row=3)
window.mainloop()
