import random
import time
import turtle
turtle.tracer(1000, 0) # Increase the first argument to speed up the drawing.
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

def drawBranch(startPosition, direction, branchLength):
    if branchLength < 5:
        # BASE CASE
        return

    # Go to the starting point & direction.
    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(direction)

    # Draw the branch (thickness is 1/7 the length).
    turtle.pendown()
    turtle.pensize(max(branchLength / 7.0, 1))
    turtle.forward(branchLength)

    # Record the position of the branch's end.
    endPosition = turtle.position()
    leftDirection = direction + random.randint(10,  30)
    leftBranchLength = branchLength - random.randint( 8,  15)
    rightDirection = direction - random.randint(10,  30)
    rightBranchLength = branchLength - random.randint( 8,  15)

    # RECURSIVE CASE
    drawBranch(endPosition, leftDirection, leftBranchLength)
    drawBranch(endPosition, rightDirection, rightBranchLength)

seed = 0
while True:
    # Get psuedorandom numbers for the branch properties.
    random.seed(seed)
    #LEFT_ANGLE     = random.randint(10,  30)
    #LEFT_DECREASE  = random.randint( 8,  15)
    #RIGHT_ANGLE    = random.randint(10,  30)
    #RIGHT_DECREASE = random.randint( 8,  15)
    START_LENGTH   = random.randint(80, 120)

    # Write out the seed number.
    turtle.clear()
    turtle.penup()
    turtle.goto(10, 10)
    turtle.write('Seed: %s' % (seed))

    # Draw the tree.
    drawBranch((350, 10), 90, START_LENGTH)
    turtle.update()
    time.sleep(2)

    seed = seed + 1 # Use the next number for the next seed.

