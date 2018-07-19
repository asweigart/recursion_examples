import turtle
turtle.tracer(10, 0) # Increase the first argument to speed up the drawing.
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

MIN_SIZE = 6 # Try changing this to decrease/increase the amount of recursion.
DRAW_SOLID = True

def isTooSmall(width, height):
    # Determine if the rectangle is too small to draw.
    return width < MIN_SIZE or height < MIN_SIZE

def drawCarpet(x, y, width, height):
    # The x and y are the lower left corner of the carpet.

    # Move the pen into position.
    turtle.penup()
    turtle.goto(x, y)

    # Draw the outer rectangle.
    turtle.pendown()
    if DRAW_SOLID:
        turtle.fillcolor('black')
        turtle.begin_fill()
    turtle.goto(x, y + height)
    turtle.goto(x + width, y + height)
    turtle.goto(x + width, y)
    turtle.goto(x, y)
    if DRAW_SOLID:
        turtle.end_fill()
    turtle.penup()

    # Draw the inner rectangles.
    drawInnerRectangle(x, y, width, height)

def drawInnerRectangle(x, y, width, height):
    if isTooSmall(width, height):
        # BASE CASE
        return
    else:
        # RECURSIVE CASE

        oneThirdWidth = width / 3
        oneThirdHeight = height / 3
        twoThirdsWidth = 2 * (width / 3)
        twoThirdsHeight = 2 * (height / 3)

        # Move into position.
        turtle.penup()
        turtle.goto(x + oneThirdWidth, y + oneThirdHeight)

        # Draw the inner rectangle.
        if DRAW_SOLID:
            turtle.fillcolor('white')
            turtle.begin_fill()
        turtle.pendown()
        turtle.goto(x + oneThirdWidth, y + twoThirdsHeight)
        turtle.goto(x + twoThirdsWidth, y + twoThirdsHeight)
        turtle.goto(x + twoThirdsWidth, y + oneThirdHeight)
        turtle.goto(x + oneThirdWidth, y + oneThirdHeight)
        turtle.penup()
        if DRAW_SOLID:
            turtle.end_fill()

        # Draw the inner rectangles across the top.
        drawInnerRectangle(x, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)
        drawInnerRectangle(x + oneThirdWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)
        drawInnerRectangle(x + twoThirdsWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)

        # Draw the inner rectangles across the middle.
        drawInnerRectangle(x, y + oneThirdHeight, oneThirdWidth, oneThirdHeight)
        drawInnerRectangle(x + twoThirdsWidth, y + oneThirdHeight, oneThirdWidth, oneThirdHeight)

        # Draw the inner rectangles across the bottom.
        drawInnerRectangle(x, y, oneThirdWidth, oneThirdHeight)
        drawInnerRectangle(x + oneThirdWidth, y, oneThirdWidth, oneThirdHeight)
        drawInnerRectangle(x + twoThirdsWidth, y, oneThirdWidth, oneThirdHeight)

drawCarpet(50, 50, 600, 600)
turtle.exitonclick()
