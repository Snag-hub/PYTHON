# Write Python GUI program to create background with changing colors



from tkinter import *
from random import shuffle
import time

window = Tk()
window.geometry("700x250")

window.option_add("*Font", "aerial")


def change_color():
    colors = ['red', 'black', 'pink', 'yellow',
              'green', 'cyan', 'orange', 'brown', 'blue']
    while True:
        shuffle(colors)
        for i in range(0, len(colors)):
            window.config(background=colors[i])
            window.update()
            time.sleep(0.3)


label = Label(window, text="Hello World", bg='white')
label.pack(pady=40, padx=30)
btn = Button(window, text="Button", command=change_color)
btn.pack(pady=10)
window.mainloop()
