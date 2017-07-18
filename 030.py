# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Max number is 354294, 9^5*6 is 354294. 9^5*7 -> 413343 so 7 digits is too much
MAX = 999999
numbers = []

for number in range(10, MAX + 1):
    s_number = str(number)
    sums = 0
    for c in s_number:
        sums += int(c) ** 5
    if sums == number:
        numbers.append(number)
print(numbers)
print(sum(numbers))
