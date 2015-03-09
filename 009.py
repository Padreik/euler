# Special Pythagorean triplet
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

SUM = 1000

found = False
a = 0
max_a = math.floor(SUM / 3)

while not found and a < max_a:
    a += 1
    b = a
    max_b = math.floor((SUM - a) / 2)
    while not found and b < max_b:
        b += 1
        c = SUM - a - b
        if a**2 + b**2 == c**2:
            found = True

print("a:", a, ", b:", b, ", c:", c)
print(a * b * c)