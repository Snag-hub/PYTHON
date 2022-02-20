# Write Python GUI program that takes input string and change letter to upper case when a button is pressed.

import string
import tkinter as tk
from tkinter import *

def upper():
    label_text.set(string.get().upper())
  

window = tk.Tk()
window.title("slip17a")
window.geometry("300x250")
label_text = StringVar()
Label(window, text="Upper Case:").grid(row=1, column=0)
result= Label(window, textvariable=label_text).grid(row=1, column=1)
string = Entry(window)
string.grid(row=1, column=2)

b= Button(window, text="Upper Case", command=upper).grid(row=2, column=2)

window.mainloop()






