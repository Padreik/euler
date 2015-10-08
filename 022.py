# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

namesFile = open('022.txt', 'r')
namesFromFileStr = namesFile.read()
namesFile.close()

namesFromFile = namesFromFileStr.split(',')
names = []
for name in namesFromFile:
    names.append(name[1:-1])

names.sort()

sum = 0
asciiStart = ord('A') - 1
for order, name in enumerate(names):
    nameValue = 0
    for letter in name:
        nameValue += ord(letter) - asciiStart
    sum += nameValue * (order + 1)

print(sum)