#Add color to draw_shape function
import turtle

#Setup screen
screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Shapes")

#Define constants
TRIANGLE = 3
SQUARE = 4
PENTAGON = 5
HEXAGON = 6
HEPTAGON = 7
OCTAGON = 8
NONAGON = 9
DECAGON = 10
HENDECAGON = 11
DODECAGON = 12
TRIDECAGON = 13

def draw_shape(sides, color):
    turtle.color(color)
    for i in range(0, sides):
        turtle.fd(50)
        turtle.lt(360/sides)
    turtle.fd(50)
        
turtle.goto(-350,0)

draw_shape(TRIANGLE, "red")
draw_shape(SQUARE, "lightgreen")
draw_shape(PENTAGON, "lightblue")
draw_shape(HEXAGON, "orange")
draw_shape(HEPTAGON, "silver")
draw_shape(OCTAGON, "yellow")
draw_shape(NONAGON, "gold")
draw_shape(DECAGON, "white")
draw_shape(HENDECAGON, "lightgrey")
draw_shape(DODECAGON, "pink")
draw_shape(TRIDECAGON, "purple")

screen.mainloop()