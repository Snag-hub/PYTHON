# Write a Python GUI program to create a label and change the label font style (font name, bold, size) using tkinter module.


import tkinter as tk
window = tk.Tk()
window.title("Welcome")
window.geometry('550x200')
my_label = tk.Label(window, text="Hello World", font=("Arial Bold", 70))
my_label.grid(column=0, row=0)
window.mainloop()
