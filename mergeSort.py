import math

def mergeSort(elements):
    if len(elements) == 0 or len(elements) == 1:
        # BASE CASE
        # With only zero or one items, `elements` is already sorted.
        return elements

    # RECURSIVE CASE
    middle = math.floor(len(elements) / 2)
    left = mergeSort(elements[:middle])
    right = mergeSort(elements[middle:])

    # At this point, `left` should be sorted and `right` should be
    # sorted. We can merge them into a single sorted list.
    sortedResult = []
    leftPointer = 0
    rightPointer = 0
    while (len(sortedResult) < len(elements)):
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

    return sortedResult # Returns a sorted version of `elements`.


print(mergeSort([3,4,5,1,2,8,3,7,6]))
