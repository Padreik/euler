# You are given the following information, but you may prefer to do some research for yourself.
#
#  -  1 Jan 1900 was a Monday.
#  -  Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#  -  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

dayOfWeek = 1 # 0 for Sunday, 1 for Monday, ...
month = 0 # 0 for January, 1 for February, ...
year = 1900
sundaysFirst = 0

while year < 2001:
    month = 0
    while month < 12:
        if month == 1:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                dayInMonth = 29
            else:
                dayInMonth = 28
        elif month in [3, 5, 8, 10]:
            dayInMonth = 30
        else:
            dayInMonth = 31
        dayOfWeek = (dayOfWeek + dayInMonth) % 7
        if dayOfWeek == 0 and year > 1900:
            sundaysFirst += 1
        month += 1
    year += 1

print(sundaysFirst)