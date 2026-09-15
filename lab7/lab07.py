"""
Module for implementing Lab 07 functions.

The first function first_vowel is a helper function of the second function
pigify (which is the primary function). Function pigify converts English words
to Pig-Latin.

IMPLEMENT both functions.

While you are encouraged to test your answers, you do not need to write a unit
test.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def remove_starting_vowel(w):
    """
    Returns: the string with the first letter removed if it's a vowel.

    If the string does not start with a vowel, returns the string as-is.
    The vowels are 'aeiou'.

    Parameter w: the word to check
    Precondition: w is a nonempty string with only lowercase letters
    """
    if 'a' in w[0] or 'e' in w[0] or 'i' in w[0] or 'o' in w[0] or 'u' in w[0]:
        return w[1:]

    return w
    pass # STUB. Implement me


def pigify(w):
    """
    Returns: copy of w converted to Pig Latin

    See the lab handout for the complete rules on Pig Latin.

    Parameter w: the word to change to Pig Latin
    Precondition: w is a nonempty string with only lowercase letters
    """
    
    if 'a' in w[0] or 'e' in w[0] or 'i' in w[0] or 'o' in w[0] or 'u' in w[0]:
        return w + 'hay'
    elif 'q' in w[0] and 'u' in w[1]: # apparently there is an assumption that if it starts with q will followed by qu
        return w[2:] + 'quay'
    elif first_vowel(w) != -1:
        i = first_vowel(w)
        return w[i:] + w[:i] + 'ay'
    else:
        return w + 'ay'
    pass # STUB. Implement me


# THIS FUNCTION IS PROVIDED FOR YOU TO USE IN PIGIFY
# NOTHING NEEDED FOR IMPLEMENTATION
def first_vowel(w):
    """
    Returns: position of the first vowel; -1 if no vowels.

    Parameter w: the word to search
    Precondition: w is a nonempty string with only lowercase letters
    """
    minpos = len(w) # invalid position; currently no vowels found

    # search for a
    pos = w.find('a')
    if pos != -1 and pos < minpos: # a found and is closest
        minpos = pos

    # search for e
    pos = w.find('e')
    if pos != -1 and pos < minpos: # e found and is closest
        minpos = pos

    # search for i
    pos = w.find('i')
    if pos != -1 and pos < minpos: # i found and is closest
        minpos = pos

    # search for o
    pos = w.find('o')
    if pos != -1 and pos < minpos: # o found and is closest
        minpos = pos

    # search for u
    pos = w.find('u')
    if pos != -1 and pos < minpos: # u found and is closest
        minpos = pos

    # search for y not at front
    pos = w.find('y',1)
    if pos != -1 and pos < minpos: # u found and is closest
        minpos = pos

    # found something if minpos moved from first assignment
    return minpos if minpos != len(w) else -1
