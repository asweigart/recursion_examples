def getCombinations(chars, m):
    print('getCombinations(%s, %s)' % (chars, m))
    if m == 0:
        # BASE CASE
        return ['']
    elif chars == '':
        # BASE CASE
        return [] # TODO - add blank string here to get all possible combinations of chars.
    else:
        # RECURSIVE CASE
        result = []
        head = chars[:1]
        tail = chars[1:]
        for combo in getCombinations(tail, m - 1):
            result.append(head + combo)

        result.extend(getCombinations(tail, m))

        return result

#print(getCombinations('abcde', 0))
#print(getCombinations('abcde', 1))
#print(getCombinations('abcde', 2))
#print(getCombinations('abcde', 3))
#print(getCombinations('abcde', 4))
print(getCombinations('abcde', 5))
