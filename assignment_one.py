# remember to use comments!
import turtle
turtle.speed(10)
def make_octo():

    for f in range(6):
        turtle.color('green')
        turtle.forward(50)
        turtle.right(30)

def make_triangle():
    for y in range(3):
        turtle.right(120)
        turtle.forward(100)


for y in range(12):
    make_octo()
    turtle.right(30)
    make_octo()
for j in range(12):
    make_triangle()




turtle.exitonclick()