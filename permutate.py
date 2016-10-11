"""
Takes in a string, and finds all the possible permutations of that string.
Returns a list of those permutations
"""

def permutate(astring):
    if len(astring) == 1:
        return [astring]

    result = []
    for i, char in enumerate(astring):
        result += [char + perm for perm in permutate(astring[:i] + astring[i + 1:])]

    return result


print permutate('abc')