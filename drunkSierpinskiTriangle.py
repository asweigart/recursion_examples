import random
import turtle
turtle.tracer(1000, 0) # Increase the first argument to speed up the drawing.
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

MIN_SIZE = 4 # Try changing this to decrease/increase the amount of recursion.

DRUNKENESS = 0.001 # Increase to make more drunk. 0.01 is seriously drunk.

def midpoint(startx, starty, endx, endy):
    # Return the x, y coordinate in the middle of the four given parameters.
    xDiff = abs(startx - endx)
    yDiff = abs(starty - endy)
    return (min(startx, endx) + (xDiff / 2.0) + (random.random() * xDiff * (random.randint(-100, 100) * DRUNKENESS)),
            min(starty, endy) + (yDiff / 2.0) + (random.random() * xDiff * (random.randint(-100, 100) * DRUNKENESS)))

def isTooSmall(ax, ay, bx, by, cx, cy):
    # Determine if the triangle is too small to draw.
    width = max(ax, bx, cx) - min(ax, bx, cx)
    height = max(ay, by, cy) - min(ay, by, cy)
    return width < MIN_SIZE or height < MIN_SIZE

def drawTriangle(ax, ay, bx, by, cx, cy):
    if isTooSmall(ax, ay, bx, by, cx, cy):
        # BASE CASE
        return
    else:
        # RECURSIVE CASE
        # Draw the triangle.
        turtle.penup()
        turtle.goto(ax, ay)
        turtle.pendown()
        turtle.goto(bx, by)
        turtle.goto(cx, cy)
        turtle.goto(ax, ay)
        turtle.penup()

        # Calculate midpoints between points A, B, and C.
        mid_ab = midpoint(ax, ay, bx, by)
        mid_bc = midpoint(bx, by, cx, cy)
        mid_ca = midpoint(cx, cy, ax, ay)

        # Draw the three inner triangles.
        drawTriangle(ax, ay, mid_ab[0], mid_ab[1], mid_ca[0], mid_ca[1])
        drawTriangle(mid_ab[0], mid_ab[1], bx, by, mid_bc[0], mid_bc[1])
        drawTriangle(mid_ca[0], mid_ca[1], mid_bc[0], mid_bc[1], cx, cy)
        return

# Draw an equilateral Sierpinski triangle.
drawTriangle(50, 50, 350, 650, 650, 50)

# Draw a skewed Sierpinski triangle.
#drawTriangle(30, 250, 680, 600, 500, 80)

turtle.exitonclick()