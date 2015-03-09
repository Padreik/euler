# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

MAX = 1000
sum = 0

for i3 in range(3, MAX, 3):
    if (i3 % 5) > 0:
        sum += i3

for i5 in range(5, MAX, 5):
    sum += i5

print(sum)