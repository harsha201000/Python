from tkinter import *

window = Tk()

titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First Name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window,width=20).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last Name: ",width=20,bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window,width=20).grid(row=2,column=1)

emailLabel = Label(window,text="email: ",bg="blue",width=20).grid(row=3,column=0)
emailEntry = Entry(window,width=30).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,columnspan=2)


window.mainloop()