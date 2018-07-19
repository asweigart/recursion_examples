def getPermutations(chars):
    if chars == '':
        # BASE CASE
        return ['']
    else:
        # RECURSIVE CASE
        permutations = []
        head = chars[0]
        tail = chars[1:]
        tailPermutations = getPermutations(tail)
        for word in tailPermutations:
            for i in range(len(word) + 1):
                newPermutation = word[0:i] + head + word[i:]
                permutations.append(newPermutation)
        return permutations

print('Permutations of "abcd":')
print(','.join(getPermutations('abcd')))
