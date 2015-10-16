# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

GOAL = 1000000
string = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = []


def new_permutation(p):
    permutations.append(p)
    if len(permutations) == GOAL:
        print(''.join(str(x) for x in p))
        exit()


def permute(prefix, suffix):
    if len(suffix) == 2:
        new_permutation(prefix + suffix)
        new_permutation(prefix + suffix[1:] + suffix[:-1])
    else:
        for i, s in enumerate(suffix):
            permute(prefix + [s], suffix[0:i] + suffix[i+1:])

permute([], string)
print(len(permute))