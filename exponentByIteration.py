def exponentByIteration(a, n):
    total = 1
    for i in range(n):
        total *= a
    return total

print(exponentByIteration(3, 6))
print(exponentByIteration(10, 3))
print(exponentByIteration(17, 10))
