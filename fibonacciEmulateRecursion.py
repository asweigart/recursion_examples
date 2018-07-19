callStack = []
callStack.append({'instrPtr': 'start', 'nthNumber': 10})
returnValue = None

while len(callStack) > 0:
    nthNumber = callStack[-1]['nthNumber']
    instrPtr = callStack[-1]['instrPtr']

    if instrPtr == 'start':
        print('fibonacci(%s) called.' % (nthNumber))
        if nthNumber == 1 or nthNumber == 2:
            # BASE CASE
            print('Call to fibonacci(%s) returning 1.' % (nthNumber))

            # "Returns" the value in returnValue.
            returnValue = 1
            callStack.pop()
            continue
        else:
            # RECURSIVE CASE
            print('Calling fibonacci(%s) (nthNumber - 1).' % (nthNumber - 1))

            # "Calling" fibonacci(nthNumber - 1)
            callStack[-1]['instrPtr'] = 'after 1st recursive call'
            callStack.append({'instrPtr': 'start', 'nthNumber': nthNumber - 1})
            continue
    elif instrPtr == 'after 1st recursive call':
        # Continuation of the recursive case.
        callStack[-1]['result'] = returnValue
        print('Calling fibonacci(%s) (nthNumber - 2).' % (nthNumber - 2))

        # "Calling" fibonacci(nthNumber - 2)
        callStack[-1]['instrPtr'] = 'after 2nd recursive call'
        callStack.append({'instrPtr': 'start', 'nthNumber': nthNumber - 2})
        continue
    elif instrPtr == 'after 2nd recursive call':
        callStack[-1]['result'] = callStack[-1]['result'] + returnValue
        print('Call to fibonacci(%s) returning %s.' % (nthNumber, callStack[-1]['result']))

        # "Returns" the value in returnValue.
        returnValue = callStack[-1]['result']
        callStack.pop()
        continue

print(returnValue)
