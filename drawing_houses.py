import turtle

turtle.speed(5)
turtle.penup()
turtle.forward(-300)

turtle.pendown()

def space_house():
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()



def make_house(size,house_color,roof_color):
    turtle.fillcolor(house_color)
    turtle.begin_fill()
    for r in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    for r in range(3):
        turtle.left(120)
        turtle.forward(size)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)









for g in range (1):
    make_house(200,'green','cyan')
    space_house()
    make_house(50,'red','yellow')
    space_house()
    make_house(75,'purple','green')
    space_house()
    make_house(100,'orange','blue')






turtle.exitonclick()
