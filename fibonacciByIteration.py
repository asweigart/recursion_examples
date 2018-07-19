def fibonacci(nthNumber):
    a, b = 1, 1
    #print('a = %s, b = %s' % (a, b))
    for i in range(2, nthNumber):
        a, b = b, a + b # Get the next Fibonacci number.
        #print('a = %s, b = %s' % (a, b))
    return b

print(fibonacci(1000))
