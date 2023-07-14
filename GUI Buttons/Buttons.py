from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)


window = Tk()

photo = PhotoImage(file='like.png')

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans",30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()