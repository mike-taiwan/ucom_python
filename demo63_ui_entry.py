# encoding=UTF-8
import Tkinter
import tkFont


def callback(ev):
    label1.config(text=entry1.get())


top = Tkinter.Tk()
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
label1 = Tkinter.Label(top, text="input something", font=myCFont)
entry1 = Tkinter.Entry(top, font=myCFont)
button1 = Tkinter.Button(top, text='submit', font=myCFont)
entry1.bind('<Return>', callback)
button1.bind('<Button-1>', callback)
label1.pack()
entry1.pack()
button1.pack()
top.minsize(400, 300)
top.mainloop()
