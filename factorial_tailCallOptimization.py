def factorial(number, runningTotal=1):
    if number == 1:
        # BASE CASE
        return runningTotal
    else:
        # RECURSIVE CASE
        return factorial(number - 1, runningTotal * number)

print(factorial(10))