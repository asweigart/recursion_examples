def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

print(gcd(42, 28))
print(gcd(28, 42))
print(gcd(345, 766))
