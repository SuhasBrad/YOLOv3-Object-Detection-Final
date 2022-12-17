from tkinter import *

root_window = Tk()
root_window.title("First Program")
dimensions = '800x600'
root_window.geometry(dimensions)
label = Label(root_window, text="Are you a Geek")
label.grid()


def clicked():
    label.configure(text="I just got clicked!")


button = Button(root_window, text="Click Me", fg="red", bg="blue", command=clicked)

button.grid(column=1, row=0)
root_window.mainloop()
