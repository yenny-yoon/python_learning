import turtle
gb=turtle.Turtle()

def center_circle(target):
    target.penup()
    target.forward(200)
    target.left(90)
    target.pendown()
    target.circle(200)
    target.left(90)
    target.forward(200)
    target.pendown()

center_circle(gb)
