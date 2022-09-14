import turtle
turtle.speed(50)
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    for x in range(4):
        turtle.forward(200)
        turtle.right(90)
    if abs(pos()) < 1:
        break
end_fill()



from turtle import *
color('green')
begin_fill()
while True:
    for r in range(3):
        turtle.forward(200)
        turtle.left(120)
    if abs(pos()) < 1:
        break
end_fill()
done()

turtle.exitonclick()