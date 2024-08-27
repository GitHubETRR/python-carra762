from turtle import *

color("red")
speed(0)
ht()

def curve () :
    for i in range(202):
        right(1)
        forward(1)

fillcolor("red")
begin_fill()
left(140)
forward(145)
curve()
left(140)
curve()
forward(145)
end_fill()
