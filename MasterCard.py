from turtle import *

# Sets the window title
title("MasterCard")
setup(400,400)

# Function to draw a rectangle
def draw_rectangle():
    for i in range(2):
        forward(200)
        right(90)
        forward(100)
        right(90)

# Draw a rectangle
penup()
setposition(-100,50)
color("black")
pendown()
begin_fill()
draw_rectangle()
end_fill()

# Draw a red circle
penup()
setposition(-25,-25)
color("red")
pendown()
begin_fill()
circle(30)
end_fill()

# Draw a orange circle
penup()
setposition(20,-25)
color("orange")
pendown()
begin_fill()
circle(30)
end_fill()

# Display text MasterCard
color("white")
penup()
goto(0,-47)
pendown()
write("MasterCard", align="center", font=("Arial", 15, "normal"))
hideturtle()

mainloop()