# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import math

cache = {}
max = (0, 0)
limit = 1000000

def collatz(value):
    if value == 1:
        return 1
    if value in cache:
        return cache[value]
    if value % 2 == 0:
        c = 1 + collatz(value / 2)
    else:
        c = 1 + collatz(value * 3 + 1)
    cache[value] = c
    return c

for i in range(1,limit):
    v = collatz(i)
    if v > max[0]:
        max = (v, i)

print("Chain of {0} elements".format(max[0]))
print(max[1])