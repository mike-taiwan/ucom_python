# encoding=UTF-8
import Tkinter
import tkFont


def callback1(ev):
    label1.config(text=message % int(ev))


message = 'value=%d'
top = Tkinter.Tk()
var1 = Tkinter.IntVar()
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
label1 = Tkinter.Label(top, text=message % 0, font=myFont)
scale1 = Tkinter.Scale(top, font=myCFont, orient='h', from_=0, to=100,
                       showvalue=False, variable=var1, command=callback1)
label1.pack()
scale1.pack()
top.minsize(400, 300)
top.mainloop()