import turtle
from turtle import*
from random import randint
from winsound import*

window = turtle.Screen()
window.title("Turtle Race Game")

turtle.bgcolor("forestgreen")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE",font=('Arial',30))

#Draw the brown square
turtle.setpos(-400,-200)
turtle.color('chocolate')
turtle.begin_fill()
turtle.pendown()
for i in range(2):
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
turtle.end_fill()

stamp_size = 20
square_size = 15
finish_line = 200

turtle.color('black')
turtle.shape('square')
turtle.penup()

for i in range(11):
    turtle.setpos(finish_line,(150-(i*square_size*2)))
    turtle.stamp()
    
for j in range(11):
    turtle.setpos(finish_line+square_size,((150-square_size)-(j*square_size*2)))
    turtle.stamp()

#Turtles    
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color('red')
turtle1.shape('turtle')
turtle1.penup()
turtle1.goto(-250,150)
turtle1.pendown()

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color('blue')
turtle2.shape('turtle')
turtle2.penup()
turtle2.goto(-250,100)
turtle2.pendown()

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color('darkgreen')
turtle3.shape('turtle')
turtle3.penup()
turtle3.goto(-250,50)
turtle3.pendown()

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color('yellow')
turtle4.shape('turtle')
turtle4.penup()
turtle4.goto(-250,0)
turtle4.pendown()

turtle5 = Turtle()
turtle5.speed(0)
turtle5.color("white")
turtle5.shape('turtle')
turtle5.penup()
turtle5.goto(-250,-50)
turtle5.pendown()

turtle6 = Turtle()
turtle6.speed(0)
turtle6.color("black")
turtle6.shape('turtle')
turtle6.penup()
turtle6.goto(-250,-100)
turtle6.pendown()

turtle7 = Turtle()
turtle7.speed(0)
turtle7.color("brown")
turtle7.shape('turtle')
turtle7.penup()
turtle7.goto(-250,-150)
turtle7.pendown()

turtle8 = Turtle()
turtle8.speed(0)
turtle8.color("silver")
turtle8.shape('turtle')
turtle8.penup()
turtle8.goto(-250,20)
turtle8.pendown()

t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0

for i in range(180):
    a = randint(1,5)
    b = randint(1,5)
    c = randint(1,5)
    d = randint(1,5)
    e = randint(1,5)
    f = randint(1,5)
    g = randint(1,5)
    h = randint(1,5)
    turtle1.forward(a)
    turtle2.forward(b)
    turtle3.forward(c)
    turtle4.forward(d)
    turtle5.forward(e)
    turtle6.forward(f)
    turtle7.forward(g)
    turtle8.forward(h)
    
    t1 += a
    t2 += b
    t3 += c
    t4 += d
    t5 += e
    t6 += f
    t7 += g
    t8 += h
    
    if t1 >= 480:
        turtle1.goto(0,-160)
        turtle.goto(0,-190)
        turtle.write('Turtle 1 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
    elif t2 >= 480:
        turtle2.goto(0,-160)
        turtle.goto(0,-190)
        turtle.write('Turtle 2 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
    elif t3 >= 480:
        turtle3.goto(0,-160)
        turtle.goto(0,-190)
        turtle.write('Turtle 3 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
    elif t4 >= 480:
        turtle4.goto(0,-150)
        turtle.goto(0,-180)
        turtle.write('Turtle 4 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
    elif t5 >= 480:
        turtle5.goto(0,-160)
        turtle.goto(0,-190)
        turtle.write('Turtle 5 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
    elif t6 >= 480:
        turtle6.goto(0,-160)
        turtle.goto(0,-190)
        turtle.write('Turtle 6 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
    elif t7 >= 480:
        turtle7.goto(0,-160)
        turtle.goto(0,-190)
        turtle.write('Turtle 7 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
    elif t8 >= 480:
        turtle8.goto(0,-160)
        turtle.goto(0,-190)
        turtle.write('Turtle 8 Wins!',font=("Arial", 15))
        PlaySound("Win.wav",SND_ASYNC)
        break
    
turtle.hideturtle()
turtle.done()