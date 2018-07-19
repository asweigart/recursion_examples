def factorial(number):
    if number == 1:
        # BASE CASE
        return 1
    else:
        # RECURSIVE CASE
        return number * factorial(number - 1)
print(factorial(5))