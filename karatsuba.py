import math

# Create a cache of all single-digit multiplication products:
MULTIPLICATION_TABLE = {}
for i in range(10):
    for j in range(10):
        MULTIPLICATION_TABLE[(i, j)] = i * j

def padZeros(numberString, numZeros, insertSide):
    """Return a string padded with zeros on the left or right side."""
    if insertSide == 'left':
        return '0' * numZeros + numberString
    elif insertSide == 'right':
        return numberString + '0' * numZeros

def karatsuba(x, y):
    """Multiply two integers with the Karatsuba algorithm. Note that
    the * operator isn't used anywhere in this function."""
    assert isinstance(x, int), 'x must be an integer'
    assert isinstance(y, int), 'y must be an integer'
    x = str(x)
    y = str(y)

    # At single-digits, "multiply" the numbers with repeated addition:
    if len(x) == 1 and len(y) == 1:
        # BASE CASE
        return MULTIPLICATION_TABLE[(int(x), int(y))]

    # RECURSIVE CASE

    # Pad with prepended zeros so that x and y are the same length:
    if len(x) < len(y):
        # If x is shorter than y, pad x with zeros:
        x = padZeros(x, len(y) - len(x), 'left')
    elif len(y) < len(x):
        # If y is shorter than x, pad y with zeros:
        y = padZeros(y, len(x) - len(y), 'left')
    # At this point, x and y have the same length.

    halfOfDigits = math.floor(len(x) / 2)
    #if (len(x) % 2) != 0:
    #    halfOfDigits += 1 # Round up to the next even number.

    # Split x into halves a & b, split y into halves c & d:
    a = int(x[:halfOfDigits])
    b = int(x[halfOfDigits:])
    c = int(y[:halfOfDigits])
    d = int(y[halfOfDigits:])

    # Make the recursive calls with these halves:
    step1Result = karatsuba(a, c) # Step 1: Multiply a & c.
    step2Result = karatsuba(b, d) # Step 2: Multiply b & d.
    step3Result = karatsuba(a + b, c + d) # Step 3: Multiply a + b & c + d.

    # Step 4: Calculate Step 3 - Step 2 - Step 1:
    step4Result = step3Result - step2Result - step1Result

    # Step 5: Pad these numbers, then add them for the return value:
    step1Padding = (len(x) - halfOfDigits) + (len(x) - halfOfDigits)
    step1PaddedNum = int(padZeros(str(step1Result), step1Padding, 'right'))

    step4Padding = (len(x) - halfOfDigits)
    step4PaddedNum = int(padZeros(str(step4Result), step4Padding, 'right'))

    return step1PaddedNum + step2Result + step4PaddedNum

print('5678 x 1234 =', karatsuba(5678, 1234)) # Prints 5678 x 1234 = 7006652

"""
import random
for i in range(100000):
    x = random.randint(0, 1000000)
    y = random.randint(0, 1000000)
    assert x * y == karatsuba(x, y)
"""