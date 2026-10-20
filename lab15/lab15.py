"""
A module with several recursive functions using divide-and-conquer

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def sum_list(thelist):
    """
    Returns the sum of the integers in list thelist.

        Example: sum_list([34]) is 34
        Example: sum_list([7,34,1,2,2]) is 46

    Parameter thelist: the list to sum
    Precondition: thelist is a list of ints
    """
    if len(thelist) == 0:
        return 0

    left = thelist[0]
    right = sum_list(thelist[1:])

    return left + right


def swapcase(s):
    """
    Returns a copy of s where letter case is swapped.
    
    Upper case letters are replaced by lower case letters. Lower case letters 
    are replaced with upper case letters. Nonletters are unaffected.
    
    Example: swapcase('Hello World!') returns 'hELLO wORLD!'
    
    Precondition: s is a string (possibly empty).
    """
    if len(s) == 0:
        return ""
    first = s[0]
    if first.isupper():
        newfirst = first.lower()
    elif first.islower():
        newfirst = first.upper()
    else:
        newfirst = first
    return newfirst + swapcase(s[1:])


# OPTIONAL EXERCISES

def numberof(thelist, v):
    """
    Returns the number of times v occurs in thelist.

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter v: The value to count
    Precondition: v is an int
    """
    # HINT: Divide and conquer only applies to one of the arguments, not both
    if len(thelist) == 0:
        return 0
    
    if thelist[0] == v:
        total = 1
    else:
        total = 0

    return total + numberof(thelist[1:], v)
        


def number_not(thelist, v):
    """
    Returns the number of elements in thelist that are NOT v.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    return 0    # Stub return.  Replace this.


def prefix(s):
    """
    Returns the prefix length of s
    
    A prefix of s is a substring at the beginning of s that has only one 
    character in it.  So 'a' is the prefix of 'abc' but 'xxyz' has the 
    prefix 'xx'.
    
    Examples: 
        prefix('abc') returns 1 as the prefix is'a'
        prefix('xxxxxxyzx') returns 6 as the prefix is'xxxxxx'
        prefix('') returns 0 as the string is empty
    
    Precondition: s is a (possibly empty) string of lowercase letters
    """
    return ''   # Stub return.  Replace this.
