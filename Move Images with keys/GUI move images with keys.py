from tkinter import *

#Functions
def move_up(event):
    canvas.move(carImage,0,-10)
def move_down(event):
    canvas.move(carImage,0,10)
def move_left(event):
    canvas.move(carImage,-10,0)
def move_right(event):
    canvas.move(carImage,10,0)

#Window
window = Tk()
window.title("Racecar")

#Keyboard Functions
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

#Setup Canvas
canvas = Canvas(window,width=500,height=500)
canvas.pack()

#Images
car = PhotoImage(file='icons8-car-100.png')
window.iconphoto(True,car)

car144 = PhotoImage(file='icons8-car-144.png')
carImage = canvas.create_image(0,0,image=car144,anchor=NW)

window.mainloop()