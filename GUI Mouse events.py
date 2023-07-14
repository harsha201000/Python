from tkinter import *

def doSomething(event):
    print("Mouse coordinates :" + str(event.x)+","+str(event.y))
window = Tk()

window.bind("<Motion>",doSomething)

window.mainloop()