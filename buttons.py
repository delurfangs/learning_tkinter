from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! i clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick)
myButton.pack()


root.mainloop()