from tkinter import *
import tkinter.messagebox

def save_data():
    try:
        fileD = open("collection.txt", "a")
        fileD.write("Category: " + "%s\n" % category.get())
        fileD.write("Description: " + "%s\n" % description.get())
        fileD.write("Author: " + "%s\n" % author.get())
        fileD.write("Edition: " + "%s\n" % edition.get())
        fileD.write("Rating: " + "%s\n" % rating.get() + "\n")
        category.set("Select one")
        description.delete(0, END)
        author.delete(0, END)
        edition.delete(0, END)
        rating.set("none")
    except Exception as ex:
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex )

def read_category(file):
    category = []
    category_f = open(file)
    for line in category_f:
        category.append(line.rstrip())
    return category

app = Tk()
app.title('Books Collection')
app.geometry("400x400+200+100")

Label(app, text = "Category:").pack()
category = StringVar()
category.set("Select one")
options = read_category("category.txt")
OptionMenu(app, category, *options).pack()

Label(app, text = "\n Description:").pack()
description = Entry(app, width=40)
description.pack()

Label(app, text = "\n Author:").pack()
author = Entry(app, width=40)
author.pack()

Label(app, text = "\n Edition:").pack()
edition = Entry(app, width=40)
edition.pack()

Label(app, text = "\n Rating:").pack()
rating = StringVar()
rating.set(None)
Radiobutton(app, variable = rating, text = "Excellent", value = "Excellent").pack()
Radiobutton(app, variable = rating, text = "OK", value = "OK").pack()
Radiobutton(app, variable = rating, text = "Bad", value = "Bad").pack()

Button(app, text = "Save",  height=1, width=10, command = save_data).pack()

app.mainloop()
