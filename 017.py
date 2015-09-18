# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def WriteOneDigit(number):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    return switcher.get(number, "")

def WriteTwoDigit(number):
    if number < 10:
        return WriteOneDigit(number)
    elif number < 20:
        switcher = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
        }
        return switcher.get(number, "")
    else:
        decimal = int(str(number)[0])
        unit = int(str(number)[1])
        switcher = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
        }
        if unit == 0:
            return switcher.get(decimal, "")
        else:
            return switcher.get(decimal, "") + "-" + WriteOneDigit(unit)

def WriteThreeDigits(number):
    if number < 100:
        return WriteTwoDigit(number)
    else:
        hundred = int(str(number)[0])
        decimals = int(str(number)[1:])
        if decimals == 0:
            return WriteOneDigit(hundred) + " hundred"
        else:
            return WriteOneDigit(hundred) + " hundred and " + WriteTwoDigit(decimals)

def WriteDigits(number):
    if number < 1000:
        return WriteThreeDigits(number)
    else:
        return "one thousand"

def CountLetters(number):
    count = 0
    for letter in str(number):
        if letter.isalpha():
            count += 1
    return count

count = 0
for i in range(1, 1001):
    # print(WriteDigits(i))
    count += CountLetters(WriteDigits(i))

print(count)