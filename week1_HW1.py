import turtle
from random import randrange

tao = turtle.Turtle()
color = ["black","red","SpringGreen",
"MediumSlateBlue","Aquamarine","Gray","Wheat"]

for x in range(5):
    for i in range(5) :
        tao.left(144)
        tao.pendown()
        tao.color(color[randrange(6)])
        tao.forward(150)
    tao.color(color[randrange(6)])
    tao.circle(70,steps=5)

    tao.penup()
    tao.left(144)
    tao.forward(300)

tao.done()
