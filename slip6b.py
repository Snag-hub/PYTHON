import tkinter as tk
from tkinter import *
from tkinter.constants import *
import random
from tkinter import messagebox

def font():
    dict = {0: 'Arial', 1: 'Courier', 2: 'Times', 3: 'Helvetica'}
    fontchoice=random.choice(dict)
    print(fontchoice)
    if checkbtn1.getint(0) == 0:
        label.config(font=fontchoice)
    elif checkbtn2.getint(1) == 1:
        label.config(font='calibri')
        print("font",label.config().get("font"))
    else:
        messagebox.showerror('TKINTER FONT', 'Something went wrong')

window = tk.Tk()
window.title("Slip 6b")
window.geometry("800x600")
label = tk.Label(window, text="Font Style")
label.grid(column=0, row=0)
label.pack()
checkbtn1 = tk.Checkbutton(window, text="Font Style", height="2", width="20", onvalue=1, offvalue=0, command=font)
checkbtn1.pack()
checkbtn2 = tk.Checkbutton(window, text="Font Size", height="2", width="20")
checkbtn2.pack()
checkbtn3 = tk.Checkbutton(window, text="Font Bold", height="2", width="20")
checkbtn3.pack()

window.mainloop()