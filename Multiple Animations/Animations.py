from tkinter import *
from Ball import Ball
import time

window = Tk()
window.title("Moving Balls")

ball = PhotoImage(file='icons8-balls-60.png')
window.iconphoto(True,ball)

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volleyball = Ball(canvas,0,0,100,1,1,"white")
tennisball = Ball(canvas,0,0,50,4,3,"yellow")
basketball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volleyball.move()
    tennisball.move()
    basketball.move()
    window.update()
    time.sleep(0.01)
    
window.mainloop()