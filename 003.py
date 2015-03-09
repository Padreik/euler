# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math

NUMBER = 600851475143

def largestPrimeFactore(number):
    i = 2
    limit = number / 2
    while i < limit:
        if number % i == 0:
            return largestPrimeFactore(number / i)
        i += 1
    return number

print(largestPrimeFactore(NUMBER))