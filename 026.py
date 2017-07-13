# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

maxD = 0
maxCycle = 0
# Get d from 2 to 1000
for d in range(2, 1000):
    remainders = []
    x = remainder = 1
    # Do a manual division, get the remainder, multiply by 10 until we find a cycle
    while remainder not in remainders and remainder != 0 and x < d:
        remainders.append(remainder)
        remainder = remainder * 10 % d
        x += 1
    remainders.append(remainder)
    # Get the cycle length and save it if it's the highest
    maxCycleTmp = len(remainders) - remainders.index(remainder) - 1
    if maxCycleTmp > maxCycle:
        maxCycle = maxCycleTmp
        maxD = d
print(maxD)
