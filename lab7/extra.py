"""
Additional problem for more practice

This problem is taken from an older exam.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
import introcs
import math


# Slicing
def europeanize(date):
    """
    Returns a European version of this date (type is a string).
    
    Days and months are padded (if necessary) to become two digits each.
    
    Examples:
        europeanize('3/6/12') is '06/03/12'
        europeanize('01/29/11') is '29/01/11'
    
    Parameter date: the date to convert
    Precondition: date a string representing a US date.
    """
    x = date.index('/')
    y = date.index('/', x + 1)
    eudate = ''
    us_day = date[x+1:y]
    us_month = date[0:x]
    us_year = date[y+1:]

    if len(us_day) == 1:
        us_day = '0' + us_day

    if len(us_month) == 1:
            us_month = '0' + us_month

    eudate += us_day + '/' + us_month + '/' + us_year
    
    return eudate

    
    pass # STUB. Implement me
