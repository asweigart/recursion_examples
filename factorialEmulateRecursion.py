callStack = []
callStack.append({'instrPtr': 'start', 'number': 5})
returnValue = None

while len(callStack) > 0:
    number = callStack[-1]['number']
    instrPtr = callStack[-1]['instrPtr']

    if instrPtr == 'start':
        if number == 1:
            # BASE CASE
            returnValue = 1
            callStack.pop()
            continue
        else:
            # RECURSIVE CASE
            callStack[-1]['instrPtr'] = 'after recursive call'
            callStack.append[{'instrPtr': 'start', 'number': number - 1}]
            continue
    elif instrPtr == 'after recursive call':
        returnValue = number * returnValue
        callStack.pop()
        continue