"""
The functions for Lab 17.

These functions all require for-loops.  They include looping over lists,
nested-lists, and dictionaries.

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT ALL THREE OF THESE FUNCTIONS
def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only
    numbers in it.

    Example: row_sums([[0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]])
    returns [0.9, 1.5, 1.7]

    Example: row_sums([[0.2, 0.1], [-0.2, 0.1], [0.2, -0.1], [-0.2, -0.1]])
    returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with no header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) each row contains
    only numbers, and (3) each row is the same length.
    """
    result = []
    for list in table:
        sum = 0
        for i in range(len(list)):
            sum += list[i]
        result.append(sum)

    return result



def place_sums(table):
    """
    MODIFIES the table to add a column summing previous elements in the row.

    This function assumes that table has a header, which means the first row
    only has strings in it.  The later rows are only numbers.  This function
    adds the string 'Sum' to the first row.  For each later row, it appends
    the sum of that row.

    This is a PROCEDURE. It modifies the table, but does not return a new table.

    Example: Suppose that a is

        [['First', 'Second', 'Third'],
         [0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]]

    then place_sums(a) modifies the table a so that it is now

         [['First', 'Second', 'Third', 'Sum'],
          [0.1, 0.3, 0.5, 0.9], [0.6, 0.2, 0.7, 1.5], [0.5, 1.1, 0.1, 1.7]]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with a header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) the first row only
    contains strings (the headers) (3) each row after the first contains only
    numbers, and (4) each row is the same length.
    """
    
    table[0].append('Sum')
    for row in table[1:]:
        sum = 0
        for x in row:
            sum += x
        row.append(sum)
    
        


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This
    function returns a new dictionary with netids for keys and letter grades
    (strings) for values.  Our cut-off is 90 for an A, 80 for a B, 70 for a C,
    60 for a D.  Anything below 60 is an F.

    Example:  letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.

    Parameter adict: the dictionary of grades
    Precondition: adict is a dictionary with string keys, int values
    """
    result = {}
    for netid in adict:
        grade = adict[netid]
        if grade >= 90:
            result[netid] = 'A'
        elif grade >= 80:
            result[netid] = 'B'
        elif grade >= 70:
            result[netid] = 'C'
        elif grade >= 60:
            result[netid] = 'D'
        else:
            result[netid] = 'F'
    return result


### OPTIONAL EXERCISES ###
def crossout(table,row,col):
    """
    Returns a copy of the table, missing the given row and column.

    Example: crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
    Example: crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
    Example: crossout([[1,3],[6,2]],0,0) returns [[2]]
    Example: crossout([[6]],0,0) returns []

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.

    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table

    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    # This is easier if you loop over positions, not elements
    pass # Implement me


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This
    function averages those grades and returns a value.

    Example: letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to (55+90+86)/3 = 77.

    Parameter adict: the dictionary of grades
    Precondition: adict is a dictionary with string keys, int values
    """
    pass # Implement me


def convert_grades(adict):
    """
    MODIFIES the dictionary to replace numerical grades with letter grades.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam. This
    function replaces all numerical grades with letter grades (strings)
    for values. Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for
    a D. Anything below 60  is an F.

    This is a PROCEDURE. It modifies the dictionary, but does not return a
    new dictionary.

    Example: If a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}, letter_grades(a)
             changes a to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
    Example: If a = {}, letter_grades(a) changes a to {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    pass # Implement me


def drop_below(adict,limit):
    """
    Deletes all students in the dictionary with grades below limit.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.

    This is a PROCEDURE. It modifies the dictionary, but does not return a
    new dictionary.


    Examples: Suppose a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
        drop_below(a,60) changes a to {'abc3' : 90, 'jms45': 86}
        drop_below(a,90) changes a to {'abc3' : 90}
        drop_below(a,95) changes a to {}
        drop_below(a,50) leaves a unchanged as {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints

    Paramater limit: the cut-off boundary
    Precondition: limit is a number (int or float)
    """
    # Hint: Create a list of netids to drop, and THEN drop them
    pass # Implement me
