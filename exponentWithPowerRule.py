import math

def exponentWithPowerRule(a, n):
    # Determine all the operations that need to be performed.
    opStack = []
    while n > 1:
        if n % 2 == 0:
            # n is even
            opStack.append('square')
            n = math.floor(n / 2)
        elif n % 2 == 1:
            # n is odd
            n -= 1
            opStack.append('multiply')

    # Perform all the operations in the correct order.
    result = a # Start result at `a`
    while opStack:
        op = opStack.pop()

        if op == 'multiply':
            result *= a
        elif op == 'square':
            result **= 2

    return result

print(exponentWithPowerRule(3, 6))
print(exponentWithPowerRule(10, 3))
print(exponentWithPowerRule(17, 10))
