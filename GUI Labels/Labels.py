from tkinter import *

window = Tk()
window.title("Tiger")

photo = PhotoImage(file='Tiger.png')
icon = PhotoImage(file='Tiger.png')

window.iconphoto(True,icon)
label = Label(window,
              text="Tiger",
              font=('Arial',40,'bold'),
              fg='green',
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()
#label.place(x=0,y=0)

window.mainloop()