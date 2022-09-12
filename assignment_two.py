# remember to use comments!
import turtle

turtle.speed(10)
def makeasquare():
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
def makeatriangle():
    for c in range (3):
        turtle.forward(50)
        turtle.left(120)

for v in range(20):
    makeasquare()
    turtle.left(25)
    makeatriangle()
    turtle.left(20)


turtle.exitonclick()