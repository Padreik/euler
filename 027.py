# Euler discovered the remarkable quadratic formula:
#
# n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
# However, when n=40,40^2+40+41 = 40(40+1)+41 is divisible by 41, and certainly when
#     n=41, 41^2+41+41 is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n=0.

import math

primes = dict()
max_a = max_b = max_primes = 0


def is_prime(n):
    n = int(math.fabs(n))
    if n in primes:
        return primes[n]
    if n <= 2:
        i = True
    else:
        if n % 2 == 0:
            i = False
        else:
            i = all(n % i for i in range(3, math.ceil(math.sqrt(n)), 2))
    primes[n] = i
    return i


def quadratic(n, a, b):
    return n ** 2 + n * a + b


def find_it():
    global max_primes, max_a, max_b
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            x = quadratic(n, a, b)
            while is_prime(x):
                n += 1
                x = quadratic(n, a, b)
            if n > max_primes:
                max_primes = n
                max_a = a
                max_b = b

find_it()
print(str(max_primes) + ": " + str(max_a) + " " + str(max_b))
print(max_a * max_b)
