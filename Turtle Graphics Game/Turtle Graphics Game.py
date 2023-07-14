#Turtle Graphics Game
import turtle
import math
import random
import winsound

#Set up screen
window = turtle.Screen()
window.bgcolor("black")
window.bgpic("kbgame-bg.gif")
window.tracer(3)

#Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#Create the score variable
score = 0

#Create goals
maxGoals = 10
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

#Set speed variable
speed = 1

#Define functions
def turnleft():
    player.left(30)
    
def turnright():
    player.right(30)
    
def increasespeed():
    global speed
    speed += 1
    
def decreasespeed():
    global speed
    speed -= 1
    
def isCollision(player, goal):
    d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))
    if d < 20:
        return True
    else:
        return False
    

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        winsound.PlaySound("bouncy-sound-81173.wav",winsound.SND_ASYNC)

    #Boundary Checking
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        winsound.PlaySound("bouncy-sound-81173.wav",winsound.SND_ASYNC)

    #Move the goal
    for count in range(maxGoals):
        goals[count].forward(3)
        
        #Boundary Checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            winsound.PlaySound("bouncy-sound-81173.wav",winsound.SND_ASYNC)
        #Boundary Checking
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            winsound.PlaySound("bouncy-sound-81173.wav",winsound.SND_ASYNC)
        #Collision Checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            winsound.PlaySound("collision-83248.wav",winsound.SND_ASYNC)
            score += 1
            #Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            



delay = raw_input("Press Enter to Finish ")