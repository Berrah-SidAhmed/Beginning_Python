
from random import choice, randint
from tkinter import *

from time import strftime


import webbrowser
import string

def erox():
    webbrowser.open_new("https://www.instagram.com/e_r_o_x/")
def eroox():
    webbrowser.open_new("https://www.facebook.com/hamoda.mrg/")
def gmail():
    webbrowser.open_new("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

def generate_password():
    password_min=8
    password_max=10
    all_chars = string.ascii_letters + string.punctuation +string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)



password = Tk()

password.geometry("780x480")
password.minsize(780,480)
password.title('Password Generateur')
password.iconbitmap("12.ico")
password.config(background="#84FFD8")

frame=Frame(password,bg="#84FFD8")

#creation d'une image
w =300
h =300
image=PhotoImage(file="400.png")
canvas=Canvas(frame,width=w,height=h,bg='#84FFD8',bd=0,highlightthickness=0)
canvas.create_image(w/2,h/2,image=image)
canvas.grid(row=0,column=0)


right_frame=Frame(frame,bg='#84FFD8')

label_title=Label(right_frame,text=" Mot De Pass !",font= ("Courier", 30, "italic"),bg="#84FFD8")
label_title.pack()

password_entry=Entry(right_frame,font= ("Courier", 20),bg="#54D5DA")
password_entry.pack()

generateur_password_boutton=Button(right_frame,text=" Générer",font= ("Times", 22, "bold italic"),bg="#57A2BA",command=generate_password)
generateur_password_boutton.pack()

right_frame.grid(row=0,column=2)








picture=PhotoImage(file="fcb.png").zoom(1).subsample(10)
picture2=PhotoImage(file="inst.png").zoom(2).subsample(14)
picture3=PhotoImage(file="gmail.png").zoom(2).subsample(35)

btm=Button(password,text="|Fcb|",font=("Courier", 8 ),bg="#84FFD8",image=picture,command=eroox,relief=FLAT)
btm.place(relx=0,rely=0,anchor="nw")
btm=Button(password,text="|Inst|",font=("Courier", 7 ),bg="#84FFD8",image=picture2,command=erox,relief=FLAT)
btm.place(relx=0,rely=1,anchor="sw")
btm=Button(password,text="|Inst|",font=("Courier", 7 ),bg="#84FFD8",image=picture3,command=gmail,relief=FLAT)
btm.place(relx=1,rely=0,anchor="ne")

def clock():
    tick=strftime('%T')
    clock_label.config(text=tick)
    clock_label.after(1000,clock)
clock_label=Label(password,font= ("Courier", 15, "italic"),bg="#84FFD8",fg='black')
clock_label.place(relx=1,rely=1,anchor="se")
clock()


frame.pack(expand="YES")


password.mainloop()


from random import choice, randint
from tkinter import *

from time import strftime


import webbrowser
import string

def erox():
    webbrowser.open_new("https://www.instagram.com/e_r_o_x/")
def eroox():
    webbrowser.open_new("https://www.facebook.com/hamoda.mrg/")
def gmail():
    webbrowser.open_new("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

def generate_password():
    password_min=8
    password_max=10
    all_chars = string.ascii_letters + string.punctuation +string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)



password = Tk()

password.geometry("780x480")
password.minsize(780,480)
password.title('Password Generateur')
password.iconbitmap("12.ico")
password.config(background="#84FFD8")

frame=Frame(password,bg="#84FFD8")

#creation d'une image
w =300
h =300
image=PhotoImage(file="400.png")
canvas=Canvas(frame,width=w,height=h,bg='#84FFD8',bd=0,highlightthickness=0)
canvas.create_image(w/2,h/2,image=image)
canvas.grid(row=0,column=0)


right_frame=Frame(frame,bg='#84FFD8')

label_title=Label(right_frame,text=" Mot De Pass !",font= ("Courier", 30, "italic"),bg="#84FFD8")
label_title.pack()

password_entry=Entry(right_frame,font= ("Courier", 20),bg="#54D5DA")
password_entry.pack()

generateur_password_boutton=Button(right_frame,text=" Générer",font= ("Times", 22, "bold italic"),bg="#57A2BA",command=generate_password)
generateur_password_boutton.pack()

right_frame.grid(row=0,column=2)








picture=PhotoImage(file="fcb.png").zoom(1).subsample(10)
picture2=PhotoImage(file="inst.png").zoom(2).subsample(14)
picture3=PhotoImage(file="gmail.png").zoom(2).subsample(35)

btm=Button(password,text="|Fcb|",font=("Courier", 8 ),bg="#84FFD8",image=picture,command=eroox,relief=FLAT)
btm.place(relx=0,rely=0,anchor="nw")
btm=Button(password,text="|Inst|",font=("Courier", 7 ),bg="#84FFD8",image=picture2,command=erox,relief=FLAT)
btm.place(relx=0,rely=1,anchor="sw")
btm=Button(password,text="|Inst|",font=("Courier", 7 ),bg="#84FFD8",image=picture3,command=gmail,relief=FLAT)
btm.place(relx=1,rely=0,anchor="ne")

def clock():
    tick=strftime('%T')
    clock_label.config(text=tick)
    clock_label.after(1000,clock)
clock_label=Label(password,font= ("Courier", 15, "italic"),bg="#84FFD8",fg='black')
clock_label.place(relx=1,rely=1,anchor="se")
clock()


frame.pack(expand="YES")


password.mainloop()


