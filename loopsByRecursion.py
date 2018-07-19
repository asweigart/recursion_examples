def theLoop(i):
    if i < 4: # Stops when false.
        # RECURSIVE CASE
        # The main code:
        print(i, 'Hello!')
        theLoop(i + 1) # Increment i.
        return
    else:
        # BASE CASE
        return

theLoop(0) # Start i at 0.