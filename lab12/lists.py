"""
The list functions for Lab 12

This module contains two functions that each work with a list. Both of 
these are mutable functions.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def put_in(alist,value):
    """
    MODIFIES the sorted list to include value, resorting as necessary.
    
    This function is a PROCEDURE.  It does not return a new list.  Instead,
    it modifies the existing list.
    
    Examples:
        If a = [0,2,3,4], put_in(a,1) makes a = [0,1,2,3,4]
        If a = [0,2,3,4], put_in(a,2) makes a = [0,2,2,3,4]
        If a = [], put_in(a,3) makes a = [3]
    
    Parameter a: The list to append to
    Precondition: a is a sorted list of ints
    
    Parameter value: The value to append
    Precondition: value is an int
    """
    alist.append(value)
    alist.sort()
    pass # Implement me


def replace_first(alist,ovalue,nvalue):
    """
    MODIFIES the list so that the first appearance of ovalue becomes nvalue.

    This function is a PROCEDURE.  It does not return a new list.  Instead,
    it modifies the existing list.

    We do not guarantee that ovalue is in the list.  If it is not there, then
    the list should remain unchanged.

    Example: If alist is [5, 9, 1, 9, 7], then replace_first(alist,9,3) modifies
    the list so that alist is now [5, 3, 1, 9, 7].

    Example: If alist is [5, 9, 1, 9, 7], then replace_first(alist,3,2) does
    not modify the list at all.

    Parameter alist: the list to modify
    Precondition: alist is a list of ints

    Parameter ovalue: the value to replace
    Precondition: ovalue is an int

    Parameter nvalue: the value to substitute with
    Precondition: nvalue is an int
    """
    if ovalue in alist:
        x = alist.index(ovalue)
        alist[x] = nvalue
    

    pass # Implement me


