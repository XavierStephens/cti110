import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.color('green')
t.pencolor('black')
t.pensize(5)
t.penup()
t.left(180)
t.forward(200)
t.pendown()
t.fillcolor('red')
t.begin_fill()
for i in (1, 2, 3):
    t.right(120)
    t.forward(100)
t.end_fill()
t.fillcolor('green')
t.penup()
t.right(180)
t.forward(300)
t.left(180)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
for i in (1, 2, 3, 4):
    t.right(90)
    t.forward(100)
t.end_fill()
t.fillcolor('green')
t.penup()
t.forward(100)
t.right(90)

