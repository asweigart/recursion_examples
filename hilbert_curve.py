from turtle import *

SIZE  = 10 # (!) Try changing the line length by a litte.
ANGLE = 90 # (!) Try changing the turning angle by a litte.
LEVEL = 5  # (!) Try changing the recursive level by a litte.

bgcolor('#B20059')
pencolor('#FFE6F2')
fillcolor('#FFE6F2')

speed('fastest')
#tracer(1, 0) # (!) Try uncommenting this line to draw the shape faster.

penup()
goto(-320, 0)
pendown()

#setheading(20) # (!) Try uncommenting this line.

def hilbert_curve(level, angle):
    if level == 0:
        return

    right(angle)
    hilbert_curve(level - 1, -angle)
    forward(SIZE)
    left(angle)
    hilbert_curve(level - 1, angle)
    forward(SIZE)
    hilbert_curve(level - 1, angle)
    left(angle)
    forward(SIZE)
    hilbert_curve(level - 1, -angle)
    right(angle)

def filled_in_hilbert():
    begin_fill()
    hilbert_curve(LEVEL, ANGLE) # draw first quadrant
    forward(SIZE)

    hilbert_curve(LEVEL, ANGLE) # draw second quadrant
    left(ANGLE)
    forward(SIZE)
    left(ANGLE)

    hilbert_curve(LEVEL, ANGLE) # draw third quadrant
    forward(SIZE)

    hilbert_curve(LEVEL, ANGLE) # draw fourth quadrant
    left(ANGLE)
    forward(SIZE)
    left(ANGLE)
    end_fill()

filled_in_hilbert()
update()
exitonclick()

