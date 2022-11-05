from tkinter import *
import webbrowser


def open_photo():
    webbrowser.open_new("https://www.python.org/")
def open_zaki():
    webbrowser.open_new("https://cdn.discordapp.com/attachments/909570729144631298/1003324126963974154/12.png")

app = Tk()

app.geometry("1366x720")
app.minsize(360,280)
app.iconbitmap("12.ico")
app.title("Sidahmed")
app.config(background="#FFC3E4")


frame=Frame(app,bg="#4132AF",bd=10,relief=GROOVE)

label_title = Label(app,text="My first things !",font= ("Courier", 40, "italic"),bg="#4132AF",fg='black',)
label_title.pack(expand="YES")
label_subtitle = Label(frame,text="This is  the most beautiful thing !",font= ("Courier", 40, "italic"),bg="#FFC3E4",fg='black',)
label_subtitle.pack()


app_button=Button(frame,text='Click Here !',font= ("Courier", 25, "italic"),bg="#4132AF",fg='black',command=open_photo)
app_button.pack()

app_button1=Button(frame,text='No',font= ("Courier", 25, "italic"),bg="#4132AF",fg='black',command=open_zaki)
app_button.pack()


frame.pack(expand=YES)
app.mainloop()