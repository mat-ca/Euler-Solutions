"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

 - 1 Jan 1900 was a Monday.
 - Thirty days has September,
   April, June, and November.
   All the rest have thirty-one,
   Save February alone,
   Which has twenty-eight, rain or shine.
   And on leap years, twenty-nine.
 - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400

How many Sundays fell on the first of the month during the tentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
"""
Jan 31
Feb 289
Mar 31
Apr 30
May 31
Jun 30
Jul 31
Aug 31
Sep 30
Oct 31
Nov 30
Dec 31
"""

"""
Day count that the first of the month is on:

Non Leap
Jan 1
Feb 32
Mar 60
Apr 91
May 121
Jun 152
Jul 182
Aug 213
Sep 244
Oct 274
Nov 305
Dec 335

Leap
Jan 1
Feb 32
Mar 61
Apr 92
May 122
Jun 153
Jul 183
Aug 214
Sep 245
Oct 275
Nov 306
Dec 336
"""


def is_leap_year(year):
    """
    Given a year, determine if it is a leap year
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    non_leap_first_days = [1, 32, 60, 91, 121,
                           152, 182, 213, 244, 274, 305, 335]
    leap_first_days = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
    sum = 0
    sun_dist = 5
    for year in range(1901, 2001):
        if is_leap_year(year):
            day_range = range(1, 367)
            this_years_days = leap_first_days
        else:
            day_range = range(1, 366)
            this_years_days = non_leap_first_days
        for day in day_range:
            print()
            if sun_dist == 0:
                if day in this_years_days:
                    sum = sum + 1
                sun_dist = 6
            else:
                sun_dist = sun_dist - 1
    print(sum)


if __name__ == "__main__":
    main()
