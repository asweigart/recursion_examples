from turtle import *
import random
import time

tracer(10000, 0)

def branch(x, y, direction, branch_length):
    # if the branch is too small, just quit
    if branch_length < 5:
        return

    # draw the "trunk"
    trunk_size = max(branch_length / 7.0, 1) + random.randint(-1, 1)
    pensize(trunk_size)
    for i in range(4):
        forward(branch_length / 4.0 + random.randint(-10, 10))
        left(random.randint(-8, 8))

        if random.randint(0, 5) == 0:
            tiny_branch_angle = random.randint(-LEFT_ANGLE, RIGHT_ANGLE)
            right(tiny_branch_angle)
            branch(xcor(), ycor(), heading(), branch_length / 2)
            left(tiny_branch_angle)
            pensize(trunk_size)
            

    if random.randint(0, 5) == 0:
        branch_length = branch_length * 0.9

    # draw the two branches, which are fractal trees
    if random.randint(0, 9) != 0:
        left(LEFT_ANGLE)
        branch(xcor(), ycor(), heading(), branch_length - LEFT_DECREASE)
        right(LEFT_ANGLE)

    if random.randint(0, 9) != 0:
        right(RIGHT_ANGLE)
        branch(xcor(), ycor(), heading(), branch_length - RIGHT_DECREASE)
        left(RIGHT_ANGLE)

    # return back to the starting point
    penup()
    goto(x, y)
    setheading(direction)
    pendown()

def draw_tree(x, y, direction, seed):
    global LEFT_ANGLE, RIGHT_ANGLE, LEFT_DECREASE, RIGHT_DECREASE

    # go to the starting point
    penup()
    goto(x, y)
    setheading(direction)
    pendown()
    
    # try changing these values and looking at the results
    random.seed(seed)
    LEFT_ANGLE     = random.randint(10,  30)
    RIGHT_ANGLE    = random.randint(10,  30)
    LEFT_DECREASE  = random.randint( 6,  15)
    RIGHT_DECREASE = random.randint( 6,  15)
    START_SIZE     = random.randint(80, 120)

    branch(x, y, direction, START_SIZE)
    update()

draw_tree(0, -310, 90, 12393)
exitonclick()
