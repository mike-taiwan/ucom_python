# encoding=UTF-8
import Tkinter
import tkFont


def callback1(ev):
    label.config(text="enter event:", bg='#F00')


def callback2(ev):
    label.config(text="leave event:", bg='#0F0')


def callback3():
    label.config(text='clicked', bg='#FFF')


top = Tkinter.Tk()
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
label = Tkinter.Label(top, text='display callback', bg='#FFF', font=myFont)
button = Tkinter.Button(top, text='click me', font=myCFont, command=callback3)
label.pack()
button.pack()
button.bind('<Enter>', callback1)
button.bind('<Leave>', callback2)

top.minsize(400, 300)
top.mainloop()