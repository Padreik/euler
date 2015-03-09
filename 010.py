# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math

MAX = 2000000
primes_sum = 2
prime = 3

while prime < MAX:
    is_prime = True
    for sub_prime in range(3, math.floor(math.sqrt(prime)) + 1):
        if prime % sub_prime == 0:
            is_prime = False
            break
    if is_prime:
        primes_sum += prime
    prime += 2

print(primes_sum)