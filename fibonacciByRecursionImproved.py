fibonacciCache = {} # Create the global cache.

def fibonacci(nthNumber):
    print('fibonacci(%s) called.' % (nthNumber))

    if nthNumber in fibonacciCache:
        # If the value was already cached, return it.
        return fibonacciCache[nthNumber]

    if nthNumber == 1 or nthNumber == 2:
        # BASE CASE
        print('Call to fibonacci(%s) returning 1.' % (nthNumber))
        fibonacciCache[nthNumber] = 1 # Update the cache.
        return 1
    else:
        # RECURSIVE CASE
        print('Calling fibonacci(%s) (nthNumber - 1).' % (nthNumber - 1))
        result = fibonacci(nthNumber - 1)

        print('Calling fibonacci(%s) (nthNumber - 2).' % (nthNumber - 2))
        result = result + fibonacci(nthNumber - 2)

        print('Call to fibonacci(%s) returning %s.' % (nthNumber, result))
        fibonacciCache[nthNumber] = result # Update the cache.
        return result

print(fibonacci(10))
