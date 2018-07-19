import turtle
turtle.tracer(1000, 0) # Increase the first argument to speed up the drawing.
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()


def pointAlongLine(startPosition, endPosition, howFar):
    # Return the x, y coordinate in the middle of the four given parameters.
    startx, starty = startPosition
    endx, endy = endPosition
    xDiff = abs(startx - endx)
    yDiff = abs(starty - endy)
    return (min(startx, endx) + (xDiff * howFar), min(starty, endy) + (yDiff * howFar))


def drawSide(startPosition, direction, length):
    if length < 1:
        # BASE CASE
        return

    # Draw the first third of the line.
    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.forward(length / 3)

    firstRecursePosition = turtle.position()
    turtle.left(60)
    firstRecurseDirection = turtle.heading()
    turtle.right(60)

    # Move to the start of the last third of the line.
    turtle.penup()
    turtle.forward(length / 3)

    # Get the second recurse info.
    turtle.right(60)
    turtle.back(length / 3)
    secondRecursePosition = turtle.position()
    secondRecurseDirection = turtle.heading()
    turtle.forward(length / 3)
    turtle.left(60)

    # Draw the last third of the line.
    turtle.pendown()
    turtle.forward(length / 3)
    turtle.penup()

    # RECURSIVE CASE
    drawSide(firstRecursePosition, firstRecurseDirection, length / 3)
    drawSide(secondRecursePosition, secondRecurseDirection, length / 3)


def drawSnowflake(startPosition, direction, length):
    startPositions = []
    directions = []

    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(direction)

    for i in range(6):
        turtle.forward(length)
        turtle.right(60)
        startPositions.append(turtle.position())
        directions.append(turtle.heading())

    for i in range(6):
        drawSide(startPositions[i], directions[i], length)

drawSnowflake((200, 600), 0, 300)
turtle.exitonclick()
