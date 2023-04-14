#CTI-110
#P4LAB1a - Turtle Initials
#Xavier Stephens
#4/14/2023
#
import turtle
win = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.pensize(15)
t.fillcolor('green')
t.pencolor('pink')
#X
t.penup()
t.left(90)
t.left(110)
t.forward(200)
t.pendown()
t.right(150)
t.forward(200)
t.penup()
t.backward(100)
t.left(80)
t.forward(100)
t.pendown()
t.right(180)
t.forward(200)
#moving
t.penup()
t.left(50)
t.forward(110)
t.pendown()
#S
t.forward(85)
t.left(90)
t.forward(75)
t.left(90)
t.forward(85)
t.right(90)
t.forward(75)
t.right(90)
t.forward(85)
t.penup()
#return to origin
t.goto(0, 0)
t.left(90)
