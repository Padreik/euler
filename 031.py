# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

MAX = 200
count = 0
coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()


def cumulate(index, amounts):
    global count
    sums = sum(a*b for a, b in zip(coins, amounts))
    if sums == MAX:
        count += 1
    elif sums < MAX:
        a2 = list(amounts)
        a2[index] += 1
        cumulate(index, a2)
        if index < len(coins) - 1:
            cumulate(index + 1, list(amounts))

cumulate(0, [0, 0, 0, 0, 0, 0, 0, 0])
print(count)
