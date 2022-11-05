from tkinter import *

from time import strftime
import webbrowser



erox = Tk()
erox.title('Sidahmed')
erox.geometry('720x480')
erox.iconbitmap("12.ico")
erox.minsize(720,480)
erox.config(background='#000000')



frame=Frame(erox)

title=Label(frame,text='Clock',font=("Times", 25, "bold italic"),background='black',foreground='#5C5C5F')
title.pack(expand=YES)



def clock():
    tick=strftime('%T')
    clock_label.config(text=tick)
    clock_label.after(1000,clock)
clock_label=Label(frame,font=("Times",80,"bold italic"),background='black',foreground='#5C5C5F')
clock_label.pack(expand=YES)
clock()




frame.pack(expand=YES)
erox.mainloop()