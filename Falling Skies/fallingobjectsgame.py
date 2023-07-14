#Falling Objects in Python 3
#Microsoft Windows 10 Home
#Python 3.11.4

import turtle
import random
import winsound

score = 0
lives = 10

window = turtle.Screen()
window.title("Catching Objects Game")
window.setup(width=800,height=600)
window.bgpic("background.gif")
window.bgcolor("green")
window.tracer(0)

window.register_shape("deer-left.gif")
window.register_shape("deer-right.gif")
window.register_shape("nut.gif")
window.register_shape("hunter.gif")


#Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("deer-right.gif")
player.color("white")
player.penup()
player.goto(0, -250)


#Create a list of good guys
good_guys = []

#Add the good_guys
for _ in range(6):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("nut.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(0, 250)
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)
    
#Create a list of bad guys
bad_guys = []

#Add the bad_guys
for _ in range(5):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("hunter.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(0, 250)
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy)
    
#Make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 25, "normal"))
    
#Functions
def go_left():
    x = player.xcor()
    x -= 5
    player.setx(x)
    player.shape("deer-left.gif")
        
def go_right():
    x = player.xcor()
    x += 5
    player.setx(x)
    player.shape("deer-right.gif")

    
#Keyboard bindings
window.listen()
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")


while True:
    #update the window
    window.update()
    
    #Move the good_guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)
        
        #Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            
        #Check for a collision with the player
        if good_guy.distance(player) < 40:
            winsound.PlaySound("power_up.wav",winsound.SND_ASYNC)
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 25, "normal"))
            
    #Move the bad_guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)
        
        #Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            
        #Check for a collision with the player
        if bad_guy.distance(player) < 20:
            winsound.PlaySound("gong.wav",winsound.SND_ASYNC)
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 5
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 25, "normal"))