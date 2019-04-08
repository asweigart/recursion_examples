def quicksort(items, left=None, right=None):
    # By default, `left` and `right` span the entire range of `items`.
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1 # `right` defaults to the last index in items.

    # UNCOMMENT FOR DEBUG OUTPUT:
    #print('quicksort() called, sorting this range:', items[left:right + 1])

    if right <= left:
        # With only zero or one items, `items` is already sorted.
        return # BASE CASE

    i = left # i starts at the beginning of the range.
    pivotIndex = right # The pivot is the value at the end of the range.
    pivotValue = items[pivotIndex]

    # UNCOMMENT FOR DEBUG OUTPUT:
    #print('                          The pivot is:', pivotValue)

    # Iterate up to, but not including, the pivot:
    for j in range(left, right):
        # If a value is less than the pivot, swap it so that it's on the
        # left side of `items`:
        if items[j] <= pivotValue:
            # Swap these two values:
            items[i], items[j] = items[j], items[i]
            i += 1

    # Put the pivot on the left side of `items`:
    items[i], items[pivotIndex] = items[pivotIndex], items[i]
    pivotIndex = i

    # UNCOMMENT FOR DEBUG OUTPUT:
    #print('           After sorting, the range is:', items[left:right + 1])

    # Call quicksort() on the left and right sides of `items`:
    quicksort(items, left, pivotIndex - 1)  # RECURSIVE CASE
    quicksort(items, pivotIndex + 1, right) # RECURSIVE CASE

myList = [0, 7, 9, 6, 3, 1, 8, 2, 5, 4]
quicksort(myList)
print(myList) # Prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
