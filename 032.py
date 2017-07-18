# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
#    the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
#     1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
#     pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

products = []
possibilities = [1, 2, 3]

max = 9876
for i in range(1, max):
    for j in range(i + 1, max + 1):
        k = i * j

        combined = str(i) + str(j) + str(k)
        if len(combined) > 9:
            break
        elif len(combined) < 9:
            continue

        isPandigital = True
        for x in range(1, len(combined) + 1):
            if str(x) not in combined:
                isPandigital = False
                break
        if isPandigital and k not in products:
            products.append(k)

print(sum(products))
