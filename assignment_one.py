# remember to use comments!
import turtle
turtle.speed(20)

turtle.penup() #changes the point where the first mosaic
turtle.goto(0,100)
turtle.pendown()
def make_octo(): #defines an octogon
    for f in range(6):
        turtle.color('green')
        turtle.forward(50)
        turtle.right(30)

def make_triangle(): #defines triangle
    for y in range(3):
        turtle.color('blue')
        turtle.right(120)
        turtle.forward(100)

def make_diamond(): #defines diamond
    for k in range(4):
        turtle.color('pink')
        turtle.forward(50)
        turtle.left(125)
        turtle.forward(50)
        turtle.left(55)
def make_penagon(): #defines penagon
    for p in range(5):
        turtle.color('purple')
        turtle.forward(75)
        turtle.left(72)




for y in range(12):  #creates first mosaic
    make_octo()
    make_triangle()
    turtle.right(30)
    make_octo()

turtle.penup() #changes position to start next mosaic
turtle.goto(-100,200)
turtle.pendown()

for j in range(12): #starts second mosaic
    make_diamond()
    make_penagon()
    turtle.right(30)

turtle.exitonclick()