def quicksort(theList, left=None, right=None):
    # By default, `left` and `right` span the entire range of `theList`.
    if left is None:
        left = 0
    if right is None:
        right = len(theList) - 1

    # UNCOMMENT FOR DEBUG OUTPUT:
    #print('quicksort() called, sorting this range:', theList[left:right + 1])

    if right <= left:
        return # BASE CASE

    i = left # i starts at the beginning of the range.
    pivotIndex = right # The pivot is the value at the end of the range.
    pivotValue = theList[pivotIndex]

    # UNCOMMENT FOR DEBUG OUTPUT:
    #print('                          The pivot is:', pivotValue)

    # Iterate up to, but not including, the pivot:
    for j in range(left, right):
        # If a value is less than the pivot, swap it so that it's on the
        # left side of `theList`:
        if theList[j] <= pivotValue:
            # Swap these two values:
            theList[i], theList[j] = theList[j], theList[i]
            i += 1

    # Put the pivot on the left side of `theList`:
    theList[i], theList[pivotIndex] = theList[pivotIndex], theList[i]
    pivotIndex = i

    # UNCOMMENT FOR DEBUG OUTPUT:
    #print('           After sorting, the range is:', theList[left:right + 1])

    # Call quicksort() on the left and right sides of `theList`:
    quicksort(theList, left, pivotIndex - 1)  # RECURSIVE CASE
    quicksort(theList, pivotIndex + 1, right) # RECURSIVE CASE

myList = [0, 7, 9, 6, 3, 1, 8, 2, 5, 4]
quicksort(myList)
print(myList) # Prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
