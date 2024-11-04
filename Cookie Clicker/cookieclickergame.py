# Cookie Clicker Game in Python
# Simple Cookie Clicker Clone
# Python 3.x Compatible
# Windows, Mac, and Linux Compatible
# by Harsha Malipeddi

import turtle
import winsound

window = turtle.Screen()
window.title("Cookie Clicker Game")
window.bgcolor("black")
window.setup(width=800, height=600)

window.register_shape("cookie.gif")

clicks = 0

cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,200)
pen.write("Clicks: {}".format(clicks), align="center", font=("Courier New", 30, "normal"))

win_pen = turtle.Turtle()
win_pen.hideturtle()
win_pen.color("white")
win_pen.penup()
win_pen.goto(0,-200)
win_pen.write("You Win!", align="center", font=("Courier New", 30, "normal"))
win_pen.clear()

def clicked(x, y):
    global clicks
    winsound.PlaySound("cookie_click.wav", winsound.SND_ASYNC)
    clicks += 1
    pen.clear()
    pen.write("Clicks: {}".format(clicks), align="center", font=("Courier New", 30, "normal"))
    if clicks == 10:
        win_pen.showturtle()
        winsound.PlaySound("tadaa.wav", winsound.SND_ASYNC)
        win_pen.write("You Win!", align="center", font=("Courier New", 30, "normal"))
        turtle.done()
    
    
cookie.onclick(clicked)


window.mainloop()