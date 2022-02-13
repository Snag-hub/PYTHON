# Write a Python GUI program to calculate volume of Sphere by accepting radius as input.


from tkinter import *


def calculate():
    # get the value from the entry box
    radius = float(e.get())
    # calculate the volume
    volume = (4/3)*3.14*radius**3
    # display the result
    lbl.configure(text="Volume of Sphere: " + str(volume))
    

window = Tk()
window.title("Volume of Sphere")
window.geometry("300x200")
lbl = Label(window, text="Volume of Sphere: ")
lbl.grid(column=1, row=4)
e = Entry(window, width=10)
e.grid(column=1, row=1)
btn = Button(window, text="Calculate", command=calculate)
btn.grid(column=1, row=2)
window.mainloop()
