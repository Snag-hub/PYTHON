# Write a Python GUI program to accept dimensions of a cylinder and display the surface area and volume of cylinder.


from tkinter import *



def volume():
  result = float(r1.get())*float(r1.get())*float(h1.get())
  myText.set(result)

def SurfaceArea():
  result = float(r1.get())*float(r1.get())*3.14
  myText1.set(result)


root = Tk()
root.title("Volume and Surface Area")
root.geometry("300x250")
myText = StringVar()
myText1=StringVar()

Label(root, text="Height of cylinder").grid(row=0, column=0)
Label(root, text="Radius of cylinder").grid(row=1, column=0)

Label(root, text="Volume:").grid(row=2, column=0)
Label(root, text="Surface Area:").grid(row=3, column=0)

result= Label(root, textvariable=myText).grid(row=2, column=1)
result1= Label(root, textvariable=myText1).grid(row=3, column=1)

r1= Entry(root)
h1= Entry(root)
r1.grid(row=0, column=1)
h1.grid(row=1, column=1)

b = Button(root, text="Volume", command=volume).grid(row=4, column=0)
b1 = Button(root, text="Surface Area", command=SurfaceArea).grid(row=4, column=1)

root.mainloop()
