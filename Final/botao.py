#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("600x250")

win.resizable(False, False)

Button(win, text="Button-1",height= 5, width=10).pack()
Button(win, text="Button-2",height=8, width=15).pack()
Button(win, text= "Button-3",height=10, width=30).pack()

win.mainloop()
