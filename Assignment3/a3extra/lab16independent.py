def remove_dups(thelist):
    """
    Returns a COPY of thelist with adjacent duplicates removed.
    
    Example: for thelist = [1,2,2,3,3,3,4,5,1,1,1]
    the answer is [1,2,3,4,5,1]
    
    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints
    """
    if len(thelist) == 0:
        return []
    if len(thelist) == 1:
        return thelist
    if thelist[0] == thelist[1]:
        return remove_dups(thelist[1:])
    else:
        return [thelist[0]] + remove_dups(thelist[1:])

def oddsevens(thelist):
    """
    Returns a COPY of the list with odds at front, evens in the back.
    
    Odd numbers are in the same order as thelist. Evens are reversed.
    
    Example: 
        oddsevens([3,4,5,6]) returns [3,5,6,4].
        oddsevens([2,3,4,5,6]) returns [3,5,6,4,2].
        oddsevens([1,2,3,4,5,6]) returns [1,3,5,6,4,2].
    
    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints (may be empty)
    """
    if len(thelist) == 0:
        return []
    if len(thelist) == 1:
        return thelist

    left = oddsevens(thelist[1:])

    if thelist[0] % 2 == 1:
        return [thelist[0]] + left
    else:
        return left + [thelist[0]]
    