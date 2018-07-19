def exponentByIteration(a, n):
    total = 1
    for _ in range(n):
        total = total * a
    return total

def exponentByRecursion(a, n):
    if n == 0:
        return 1 # BASE CASE
    elif n == 1:
        return a # BASE CASE
    elif n % 2 == 0:
        res = exponentByRecursion(a, n // 2)
        return res * res
    else:
        res = exponentByRecursion(a, n // 2)
        return res * res * a

def exponentsByIteration_Improved(a, n):
    total = 1
    while n > 1:
        total = 0

import cProfile
print('Calling exponentByIteration(2, 1000000)...')
cProfile.run('exponentByIteration(2, 1000000)')
print('Calling exponentByRecursion(2, 1000000)...')
cProfile.run('exponentByRecursion(2, 1000000)')

