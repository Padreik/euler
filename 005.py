# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

MAX = 20
jump = MAX * MAX - 1
multiple_found = False
i = 0

while not multiple_found:
    i += jump
    multiple_found = True
    for j in range(MAX - 2, 0, -1):
        if i % j > 0:
            multiple_found = False
            break

print(i)