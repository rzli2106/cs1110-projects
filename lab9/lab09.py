"""
Module for implementing Lab 09 functions.

This module uses the Time class provided by the module time.  It contains two  
functions: add_time1, add_time2.  You are to implement these functions.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
from clock import Time


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object
    
    DO NOT ALTER time1 or time2, even though they are mutable
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    x = Time(0,0)
    if time1.minutes + time2.minutes < 60:
        x.minutes = time1.minutes + time2.minutes
    else:
        x.minutes = (time1.minutes + time2.minutes)%60
        x.hours += 1
    x.hours += time1.hours + time2.hours

    return x


def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2
    
    DO NOT RETURN a new time object. Modify the object time1 instead.
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    
    if time1.minutes + time2.minutes < 60:
        time1.minutes = time1.minutes + time2.minutes
    else:
        time1.minutes = (time1.minutes + time2.minutes)%60
        time1.hours += 1
    time1.hours += time2.hours

