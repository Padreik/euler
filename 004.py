# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

MAX = 999


def is_palindrome(n1, n2):
    result = str(n1 * n2)
    len_r = len(result)
    middle = math.floor(len_r / 2)
    pal = True
    for i in range(middle + 1):
        if result[i] != result[len_r - i - 1]:
            pal = False
            break
    return pal

min, result, r1, r2 = 0, 0, 0, 0
n1 = MAX

while n1 > min:
    n2 = MAX
    while n2 >= n1:
        if is_palindrome(n1, n2):
            if n1 * n2 > result:
                result = n1 * n2
                r1, r2 = n1, n2
            min = math.floor(result / MAX)
            break
        n2 -= 1
    n1 -= 1

print(r1, " x ", r2, " = ", result)