#Basic Animation in Python 3
import turtle
import time

window = turtle.Screen()
window.title("Animation")
window.bgcolor("black")

#Resigter shapes
window.register_shape("spaceinvader.gif")
window.register_shape("spaceinvader2.gif")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("spaceinvader.gif")
        self.color("lightgreen")
        self.frame = 0
        self.frames = ["spaceinvader.gif", "spaceinvader2.gif"]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])

player = Player()
player.animate()

player2 = Player()
player2.goto(-100,0)
player2.animate()

player3 = Player()
player3.goto(100,0)
player3.animate()
   
while True:
    window.update()
    print("mainloop")