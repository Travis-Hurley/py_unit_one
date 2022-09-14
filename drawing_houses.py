import turtle
turtle.speed(1)
turtle.penup()
turtle.forward(-300)
turtle.pendown()

def space_house():
    turtle.right(120)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()



def make_house():
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for h in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

    turtle.fillcolor('green')
    turtle.begin_fill()
    for r in range(4):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()


for g in range(4):
    make_house()
    space_house()


turtle.exitonclick()
