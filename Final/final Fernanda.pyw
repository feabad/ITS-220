from tkinter import *
import tkinter.messagebox

def save_data():
        fileD = open("collection.txt", "a")
        fileD.write("\n Category:\n " + "%s\n" % category.get())
        fileD.write("Description:\n " + "%s\n" % description.get())
        fileD.write("Author: " + "%s\n" % author.get())
        fileD.write("Edition: " + "%s\n" % edition.get())
        category.set("")
        description.delete(0, END)
        author.delete(0, END)
        edition.delete(0, END)
    
def read_category(file):
    category = []
    category_f = open(file)
    for line in category_f:
        category.append(line.rstrip())
    return category

app= Tk()
app.title('Books Collection')
app.geometry("300x300+200+100")

Label(app, text = "Category:").pack()
category = StringVar()
category.set(None)

options = read_category("category.txt")
OptionMenu(app, category, *options).pack()

Label(app, text = "\n Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Author:").pack()
author = Entry(app)
author.pack()

Label(app, text = "Edition:").pack()
edition = Entry(app)
edition.pack()



Button(app, text = "Save", height=1, width=10, command = save_data).place(x=110, y=265)

app.mainloop()
