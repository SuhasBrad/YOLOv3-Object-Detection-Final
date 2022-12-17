from tkinter import *
from tkinter.ttk import *

root_window = Tk()
root_window.title("First Program")
frame = Frame(root_window)
frame.pack()
button = Button(frame,text = "Geek")
button.pack()
label = Label(frame, text="GeeksForGeeks")
label.pack()
chk_box = Checkbutton(frame,text="Test_Run")
chk_box.pack()
# text_box = Text(frame)
# text_box.pack()
canvas = Canvas(frame)
canvas.pack()
root_window.mainloop()
