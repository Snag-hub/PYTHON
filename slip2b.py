# Write Python GUI program to create a digital clock with Tkinter to display the time.

from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title('Clock')


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(window, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')

lbl.pack()
time()

window.mainloop()
