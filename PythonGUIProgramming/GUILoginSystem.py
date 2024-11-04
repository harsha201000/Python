from tkinter import *

def submit():
    print("Accepted ✅")

window1 = Tk()
window1.geometry("402x289")
window1.title("Login System")

loginUI = PhotoImage(file="UILoginSystem.png")
window1.iconphoto(True,loginUI)

userProfilePic = PhotoImage(file="user.png")

header = Label(window1,text="Login System",font="Arial 15 bold",image=userProfilePic,compound="right")
header.pack()

name = Label(window1,text="Name")
name.place(x=50,y=50) 

email = Label(window1,text="Email")
email.place(x=50,y=100) 

password = Label(window1,text="Password")
password.place(x=50,y=150) 

name_entry = Entry(window1,text="Name")
name_entry.place(x=150,y=50) 

email_entry = Entry(window1,text="Email")
email_entry.place(x=150,y=100) 

password_entry = Entry(window1,text="Password")
password_entry.place(x=150,y=150) 

btn = Button(window1,text="Submit",command=submit)
btn.place(x=50,y=200)

window1.mainloop()