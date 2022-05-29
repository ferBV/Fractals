from turtle import *

shape("turtle")
speed(0)

penup()
goto(-100,200)
pendown()


def sausage_side(length, order):
    if order == 0:
        forward(length)
        return

    length /= 4.0

    sausage_side(length, order-1)
    left(90)
    sausage_side(length, order-1)
    right(90)
    sausage_side(length, order-1)
    right(90)
    sausage_side(length, order-1)
    sausage_side(length, order-1)
    left(90)
    sausage_side(length, order-1)
    left(90)
    sausage_side(length, order-1)
    right(90)
    sausage_side(length,order-1)


def create_sausage(sides, length, order):
    for  i in range(sides):
        sausage_side(length, order)
        right(360/sides)

create_sausage(4,400, 3)
ts = getscreen()

ts.getcanvas().postscript(file="duck.png")

mainloop()




