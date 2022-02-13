# Write a Python GUI program to create a label and change the label font style (font name, bold, size) using tkinter module.

import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter Basic exercises-")
parent.geometry("400x400")
my_label = tk.Label(parent, text="Hello", font=("Arial Bold", 80))
my_label.grid(column=1, row=1)
parent.mainloop()
