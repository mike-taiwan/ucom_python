# encoding=UTF-8
import Tkinter
import tkFont

counter = 0


def callback1():
    global counter
    label1.config(text="button clicked %d times" % counter)
    counter += 1


counterList = [0]


def callback2():
    label2.config(text='button clicked %d times' % counterList[0])
    counterList[0] += 1


top = Tkinter.Tk()
# print tkFont.families()
for f in tkFont.families():
    print f
print
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
label1 = Tkinter.Label(top, text="Hello world1", pady=30, bg='#C0FFEE', font=myFont)
label2 = Tkinter.Label(top, text="welcome", padx=30, bg='#FFEEC0', font=myFont)
label3 = Tkinter.Label(top, text='橫逸資訊', font=myCFont, fg='#990000', bg='#EEFFC0',
                       padx=20, pady=40)
button1 = Tkinter.Button(top, text='按鈕1', font=myCFont, bg='#000000', fg='#C0FFEE',
                         command=callback1)
button2 = Tkinter.Button(top, text='按鈕2', font=myCFont, bg='#0000FF', fg='#C0FF00',
                         command=callback2)

label2.pack()
label1.pack()
label3.pack()
button1.pack()
button2.pack()
top.mainloop()