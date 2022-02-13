#Write Python GUI program to add menu bar with name of colors as options to change the background color as per selection from menu option. 


from tkinter import *
app = Tk()

app.title("Geeks For Geeks")
app.geometry("800x500")

menubar = Menu(app, background='blue', fg='white')

file = Menu(menubar, tearoff=False, background='yellow')
edit = Menu(menubar, tearoff=False, background='pink')

file.add_command(label="New")
file.add_command(label="Exit", command=app.quit)

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)

app.config(menu=menubar)
app.mainloop()
