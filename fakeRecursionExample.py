# THIS IS A FAKE PROGRAM, THOUGH TECHNICALLY IT STILL WORKS.

def shortestWithBaseCase1(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.' % makeRecursiveCall)
    if not makeRecursiveCall:
        # BASE CASE
        print('Returning from base case.')
        return
    else:
        # RECURSIVE CASE
        shortestWithBaseCase2(False) # Imagine this calls the bottom shortestWithBaseCase() function.
        print('Returning from recursive case.')
        return

def shortestWithBaseCase2(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.' % makeRecursiveCall)
    if not makeRecursiveCall:
        # BASE CASE
        print('Returning from base case.')
        return # Imagine that this returns to the top shortestWithBaseCase() function.
    else:
        # RECURSIVE CASE
        shortestWithBaseCase3(False)
        print('Returning from recursive case.')
        return

print('Calling shortestWithBaseCase(False):')
shortestWithBaseCase1(False) # Imagine this calls the top shortestWithBaseCase() function.
print('\n')
print('Calling shortestWithBaseCase(True):')
shortestWithBaseCase1(True) # Imagine this calls the top shortestWithBaseCase() function.
