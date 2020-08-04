def binarySearch(items, target, start=None, end=None):
    if start is None:
        start = 0 # `start` defaults to the 0 index.
    if end is None:
        end = len(items) - 1 # `end` defaults to the last index.

    if start > end: # BASE CASE
        return None # The `target` is not in `items`.

    mid = (start + end) // 2
    if target == items[mid]: # BASE CASE
        return mid # `target` has been found in `items`
    elif target < items[mid]: # RECURSIVE CASE
        return binarySearch(items, target, start, mid - 1)
    elif target > items[mid]: # RECURSIVE CASE
        return binarySearch(items, target, mid + 1, end)

print(binarySearch([1, 4, 8, 11, 13, 16, 19, 19], 11))