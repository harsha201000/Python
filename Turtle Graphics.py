# Turtle Graphics in Python

import turtle

jacob = turtle.Turtle()
jacob.color('green')
jacob.pensize(5)
jacob.shape('turtle')

for count in range(4):
    jacob.forward(50)
    jacob.right(90)
    jacob.pendown()
    jacob.color('green')