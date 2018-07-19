import sys

# Create the image (make sure it's rectangular!)
im = [list('..########################...........'),
      list('..#......................#...#####...'),
      list('..#..........########....#####...#...'),
      list('..#..........#......#............#...'),
      list('..#..........########.........####...'),
      list('..######......................#......'),
      list('.......#..#####.....###########......'),
      list('.......####...#######................')]

HEIGHT = len(im)
WIDTH = len(im[0])

def floodFill(image, x, y, newChar, oldChar=None):
    if oldChar == None:
        # If oldChar isn't passed, assume it's the character at x, y.
        oldChar = image[y][x]
    if oldChar == newChar or image[y][x] != oldChar:
        # BASE CASE
        return

    image[y][x] = newChar # Change the character.

    # Change the neighboring characters.
    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x, y + 1, newChar, oldChar)
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x, y - 1, newChar, oldChar)
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x + 1, y, newChar, oldChar)
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        # RECURSIVE CASE
        floodFill(image, x - 1, y, newChar, oldChar)

def printImage(image):
    for y in range(HEIGHT):
        # Print each row.
        for x in range(WIDTH):
            # Print each column.
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')

printImage(im)
floodFill(im, 3, 3, 'o')
printImage(im)
