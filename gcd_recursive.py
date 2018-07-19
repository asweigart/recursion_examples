def gcd(a, b):
    a, b = b % a, a
    if a == 0:
        # BASE CASE
        return b
    else:
        # RECURSIVE CASE
        return gcd(a, b)

print(gcd(42, 28))
print(gcd(28, 42))
print(gcd(345, 766))


import random
a = random.randint(100, 200) / 17
b = random.randint(100, 200) / 17
print('%s, %s, %s' % (a, b, gcd(a,b)))