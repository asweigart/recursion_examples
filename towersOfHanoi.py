import sys

# Set up towers A, B, and C. The end of the list is the top of the tower.
TOTAL_DISCS = 6
HEIGHT = TOTAL_DISCS + 1

# Populate Tower A:
TOWERS = {'A': list(reversed(range(1, TOTAL_DISCS + 1))),
          'B': [],
          'C': []}

def printDisc(discNum):
    # Print a single disc of width discNum.
    emptySpace = ' ' * (TOTAL_DISCS - discNum)
    if discNum == 0:
        # Just draw the pole.
        sys.stdout.write(emptySpace + '||' + emptySpace)
    else:
        # Draw the disc.
        discSpace = '@' * discNum
        discNumLabel = str(discNum).rjust(2, '_')
        sys.stdout.write(emptySpace + discSpace + discNumLabel + discSpace + emptySpace)

def printTowers():
    # Print all three towers.
    for level in range(HEIGHT - 1, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisc(0)
            else:
                printDisc(tower[level])
        sys.stdout.write('\n')
    # Print the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISCS)
    print('%s A%s%s B%s%s C\n' % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

def moveOneDisc(startTower, endTower):
    # Move the top disc from startTower to endTower.
    disc = TOWERS[startTower].pop()
    TOWERS[endTower].append(disc)

def moveDiscs(numberOfDiscs, startTower, endTower, tempTower):
    # Move the top numberOfDiscs discs from startTower to endTower.
    if numberOfDiscs == 1:
        # BASE CASE
        moveOneDisc(startTower, endTower)
        printTowers()
        return
    else:
        # RECURSIVE CASE
        moveDiscs(numberOfDiscs - 1, startTower, tempTower, endTower)
        moveOneDisc(startTower, endTower)
        printTowers()
        moveDiscs(numberOfDiscs - 1, tempTower, endTower, startTower)
        return


# Solve
printTowers()
moveDiscs(TOTAL_DISCS, 'A', 'B', 'C')

# Uncomment to enable interactive mode:
#while True:
#    printTowers()
#    print('Enter letter of start tower and the end tower. (A, B, C) Or Q to quit.')
#    move = input().upper()
#    if move == 'Q':
#        sys.exit()
#    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#        moveOneDisc(move[0], move[1])

