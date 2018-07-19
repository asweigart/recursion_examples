def shortestWithBaseCase(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.' % makeRecursiveCall)
    if not makeRecursiveCall:
        # BASE CASE
        print('Returning from base case.')
        return
    else:
        # RECURSIVE CASE
        shortestWithBaseCase(False)
        print('Returning from recursive case.')
        return

print('Calling shortestWithBaseCase(False):')
shortestWithBaseCase(False)
print('\n')
print('Calling shortestWithBaseCase(True):')
shortestWithBaseCase(True)
