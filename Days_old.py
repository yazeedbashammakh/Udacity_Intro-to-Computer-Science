# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def conv(year,month,day):
    year = year - 1
    s = 365 * (year)
    s += (year / 400) + ((year/4) % 25) + (year / 4 - ((year/4) % 25))*24 / 25
    year = year+1
    l = 0
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        l = 1
    if l == 1 and month > 2:
        s += 1
    m = [31,28,31,30,31,30,31,31,30,31,30,31]
    s += sum(m[:month-1]) + day
    return s
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    return conv(year2,month2,day2) - conv(year1,month1,day1)

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
