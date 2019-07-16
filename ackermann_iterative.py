print('Starting with m = 1, n = 1:')
callStack = [{'m': 1, 'n': 1, 'indentation': 0, 'instrPtr': 'start'}]
returnValue = None

while len(callStack) != 0:
    m = callStack[-1]['m']
    n = callStack[-1]['n']
    indentation = callStack[-1]['indentation']
    instrPtr = callStack[-1]['instrPtr']

    if instrPtr == 'start':
        print('%sackermann(%s, %s)' % (' ' * indentation, m, n))

        if m == 0:
            # BASE CASE
            returnValue = n + 1
            callStack.pop()
            continue
        elif m > 0 and n == 0:
            # RECURSIVE CASE
            callStack[-1]['instrPtr'] = 'after first recursive case'
            callStack.append({'m': m - 1, 'n': 1, 'indentation': indentation + 1, 'instrPtr': 'start'})
            continue
        elif m > 0 and n > 0:
            # RECURSIVE CASE
            callStack[-1]['instrPtr'] = 'after second recursive case, inner call'
            callStack.append({'m': m, 'n': n - 1, 'indentation': indentation + 1, 'instrPtr': 'start'})
            continue
    elif instrPtr == 'after first recursive case':
        returnValue = returnValue
        callStack.pop()
        continue
    elif instrPtr == 'after second recursive case, inner call':
        callStack[-1]['innerCallResult'] = returnValue
        callStack[-1]['instrPtr'] = 'after second recursive case, outer call'
        callStack.append({'m': m - 1, 'n': returnValue, 'indentation': indentation + 1, 'instrPtr': 'start'})
        continue
    elif instrPtr == 'after second recursive case, outer call':
        returnValue = returnValue
        callStack.pop()
        continue
print(returnValue)




print('Starting with m = 2, n = 3:')
callStack = [{'m': 2, 'n': 3, 'indentation': 0, 'instrPtr': 'start'}]
returnValue = None

while len(callStack) != 0:
    m = callStack[-1]['m']
    n = callStack[-1]['n']
    indentation = callStack[-1]['indentation']
    instrPtr = callStack[-1]['instrPtr']

    if instrPtr == 'start':
        print('%sackermann(%s, %s)' % (' ' * indentation, m, n))

        if m == 0:
            # BASE CASE
            returnValue = n + 1
            callStack.pop()
            continue
        elif m > 0 and n == 0:
            # RECURSIVE CASE
            callStack[-1]['instrPtr'] = 'after first recursive case'
            callStack.append({'m': m - 1, 'n': 1, 'indentation': indentation + 1, 'instrPtr': 'start'})
            continue
        elif m > 0 and n > 0:
            # RECURSIVE CASE
            callStack[-1]['instrPtr'] = 'after second recursive case, inner call'
            callStack.append({'m': m, 'n': n - 1, 'indentation': indentation + 1, 'instrPtr': 'start'})
            continue
    elif instrPtr == 'after first recursive case':
        returnValue = returnValue
        callStack.pop()
        continue
    elif instrPtr == 'after second recursive case, inner call':
        callStack[-1]['innerCallResult'] = returnValue
        callStack[-1]['instrPtr'] = 'after second recursive case, outer call'
        callStack.append({'m': m - 1, 'n': returnValue, 'indentation': indentation + 1, 'instrPtr': 'start'})
        continue
    elif instrPtr == 'after second recursive case, outer call':
        returnValue = returnValue
        callStack.pop()
        continue
print(returnValue)