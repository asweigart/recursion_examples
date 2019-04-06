callStack = [] # The explicit call stack, which holds "frame objects".
callStack.append({'instrPtr': 'start', 'number': 5}) # "Call" the "factorial() function"
returnValue = None

while len(callStack) > 0:
    # The body of the "factorial() function":

    number = callStack[-1]['number'] # Set number parameter.
    instrPtr = callStack[-1]['instrPtr']

    if instrPtr == 'start':
        if number == 1:
            # BASE CASE
            returnValue = 1
            callStack.pop() # "Return" from "function call".
            continue
        else:
            # RECURSIVE CASE
            callStack[-1]['instrPtr'] = 'after recursive call'
            # "Call" the "factorial() function":
            callStack.append({'instrPtr': 'start', 'number': number - 1})
            continue
    elif instrPtr == 'after recursive call':
        returnValue = number * returnValue
        callStack.pop()  # "Return from function call".
        continue

print(returnValue)

