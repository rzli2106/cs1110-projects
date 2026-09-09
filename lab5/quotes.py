'''
The module for first_inside_quotes

Richard Li
Sept 8 2026
'''


# Add the function first_inside_quotes here
def first_inside_quotes(s):
   """
   Returns the first substring of s between two (double) quotes

   A quote character is one that is inside a string, not one that
   delimits it.  We typically use single quotes (') to delimit a
   string if want to use a double quote character (") inside of it.

   Examples:
   first_inside_quotes('A "B C" D') returns 'B C'
   first_inside_quotes('A "B C" D "E F" G') also returns 'B C',
   because it only picks the first such substring

   Parameter s: a string to search
   Precondition: s is a string containing at least two double quotes
   """
   x = s.find('"')
   y = s.find('"', x+1)

   result = s[x+1:y]

   return result
