"""
Unit test script for Lab 15

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 13, 2026
"""
import introcs
import lab15


def test_sum_list():
    """
    Tests for function sum_list
    """
    print('Testing sum_list')
    introcs.assert_equals(0,  lab15.sum_list([]))
    introcs.assert_equals(34, lab15.sum_list([34]))
    introcs.assert_equals(46, lab15.sum_list([7,34,1,2,2]))


def test_swapcase():
    """
    Tests for function swapcase
    """
    print('Testing swapcase')
    introcs.assert_equals('',       lab15.swapcase(''))
    introcs.assert_equals('a',      lab15.swapcase('A'))
    introcs.assert_equals('A',      lab15.swapcase('a'))
    introcs.assert_equals('123',    lab15.swapcase('123'))
    introcs.assert_equals('hELLO',  lab15.swapcase('Hello'))
    introcs.assert_equals('hELLO wORLD', lab15.swapcase('Hello World'))


### OPTIONAL EXERCISES ###

def test_numberof():
    """
    Tests for function numberof
    """
    print('Testing numberof')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals(0, lab15.numberof([],4))
    introcs.assert_equals(1, lab15.numberof([4],4))
    introcs.assert_equals(3, lab15.numberof(mylist,74))
    introcs.assert_equals(2, lab15.numberof(mylist,3))
    introcs.assert_equals(0, lab15.numberof(mylist,4))


def test_number_not():
    """
    Tests for function number_not
    """
    print('Testing number_not')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals(0, lab15.number_not([],4))
    introcs.assert_equals(0, lab15.number_not([4],4))
    introcs.assert_equals(4, lab15.number_not(mylist,74))
    introcs.assert_equals(5, lab15.number_not(mylist,3))
    introcs.assert_equals(7, lab15.number_not(mylist,4))


def test_prefix():
    """
    Tests for function prefix
    """
    print('Testing prefix')
    introcs.assert_equals(0, lab15.prefix(''))
    introcs.assert_equals(1, lab15.prefix('abc'))
    introcs.assert_equals(1, lab15.prefix('ababa'))
    introcs.assert_equals(2, lab15.prefix('aaba'))
    introcs.assert_equals(4, lab15.prefix('xxxxyz'))
    introcs.assert_equals(1, lab15.prefix('xyyyyyz'))


# Script Code
if __name__ == '__main__':
    test_sum_list()
    test_swapcase()

    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_numberof()
    #test_number_not()
    #test_prefix()

    print('Module lab15 passed all tests.')
