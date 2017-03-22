# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(second):
    hours = second / 3600
    second = second % 3600
    minute = second / 60
    second = second % 60
    s = str(int(hours))
    if int(hours) == 1 :
        s = s + ' hour, '
    else:
        s = s + ' hours, '
    s = s + str(int(minute))
    if int(minute) == 1 :
        s = s + ' minute, '
    else:
        s = s + ' minutes, '
    s = s + str(second)
    if 0 < second <= 1 :
        s = s + ' second '
    else:
        s = s + ' seconds '
    
    return s

print convert_seconds(60)
#>>> 0 hours, 1 minute, 0 seconds

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
