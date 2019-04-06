import math

def mergeSort(items):
    # UNCOMMENT FOR DEBUG OUTPUT:
    print(' mergeSort() called on:', items)

    if len(items) == 0 or len(items) == 1:
        # BASE CASE
        # With only zero or one items, `items` is already sorted.
        return items

    # RECURSIVE CASE
    middle = math.floor(len(items) / 2)

    # UNCOMMENT FOR DEBUG OUTPUT:
    print('            Split into:', items[:middle], 'and', items[middle:])

    left = mergeSort(items[:middle])
    right = mergeSort(items[middle:])

    # At this point, `left` should be sorted and `right` should be
    # sorted. We can merge them into a single sorted list.
    sortedResult = []
    leftPointer = 0
    rightPointer = 0
    while (len(sortedResult) < len(items)):
        if left[leftPointer] < right[rightPointer]:
            sortedResult.append(left[leftPointer])
            leftPointer += 1
        else:
            sortedResult.append(right[rightPointer])
            rightPointer += 1

        # If one of the pointers has reached the end of its list,
        # put the rest of the other list into `sortedResult`.
        if leftPointer == len(left):
            sortedResult.extend(right[rightPointer:])
            break
        elif rightPointer == len(right):
            sortedResult.extend(left[leftPointer:])
            break

    # UNCOMMENT FOR DEBUG OUTPUT:
    print('Two halves sorted into:', sortedResult)

    return sortedResult # Returns a sorted version of `items`.

myList = [0, 7, 9, 6, 3, 1, 8, 2, 5, 4]
myList = mergeSort(myList)
print(myList)