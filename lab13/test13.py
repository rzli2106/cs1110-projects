"""
A unit test for Lab 13

Author: Walker M. White (wmw2)
Date:   October 20, 2018
"""
import introcs
import lab13


def test_lesser_than():
    """
    Test procedure for function lesser_than
    """
    print('Testing function lesser_than')
    thelist = [5, 9, 5, 7, 3, 10, 4]
    introcs.assert_equals(2,lab13.lesser_than(thelist,5))
    introcs.assert_equals(1,lab13.lesser_than(thelist,4))
    introcs.assert_equals(0,lab13.lesser_than(thelist,3))
    introcs.assert_equals(4,lab13.lesser_than(thelist,6))
    introcs.assert_equals(6,lab13.lesser_than(thelist,10))
    introcs.assert_equals(7,lab13.lesser_than(thelist,20))


def test_clamp():
    """
    Test procedure for function clamp
    """
    print('Testing function clamp')
    
    thelist = [-1, 1, 3, 5]
    lab13.clamp(thelist,0,4)
    introcs.assert_equals([0,1,3,4],thelist)
    
    thelist = [1, 3]
    lab13.clamp(thelist,0,4)
    introcs.assert_equals([1,3],thelist)
    
    thelist = [-1, 1, 3, 5]
    lab13.clamp(thelist,1,1)
    introcs.assert_equals([1,1,1,1],thelist)
    
    thelist = []
    lab13.clamp(thelist,0,4)
    introcs.assert_equals([],thelist)


### OPTIONAL EXERCISES ###

def test_devowel():
    """
    Test procedure for function devowel
    """
    print('Testing function devowel')
    introcs.assert_equals('ppl',lab13.devowel('apple'))
    introcs.assert_equals('bl',lab13.devowel('boil'))
    introcs.assert_equals('yrn',lab13.devowel('yearn'))
    introcs.assert_equals('bsnss',lab13.devowel('business'))
    introcs.assert_equals('mplfy',lab13.devowel('amplify'))


def test_uniques():
    """
    Test procedure for function uniques
    """
    print('Testing function uniques')
    thelist = [5, 9, 5, 7] 
    introcs.assert_equals(3,lab13.uniques(thelist))
    
    thelist = [5, 5, 1, 'a', 5, 'a']
    introcs.assert_equals(3,lab13.uniques(thelist))
    
    thelist = [1, 2, 3, 4, 5]
    introcs.assert_equals(5,lab13.uniques(thelist))
    
    thelist = []
    introcs.assert_equals(0,lab13.uniques(thelist))
    
    # Make sure the function does not modify the original
    thelist = [5, 9, 5, 7]
    result  = lab13.uniques(thelist)
    introcs.assert_equals([5, 9, 5, 7],thelist)


def test_removeall():
    """
    Test procedure for removeall
    """
    print('Testing function removeall')
    
    alist = [1,2,2,3,1]
    result = lab13.removeall(alist,1)
    introcs.assert_equals([2,2,3],result)
    introcs.assert_equals([1,2,2,3,1],alist)
    
    result = lab13.removeall(alist,2)
    introcs.assert_equals([1,3,1],result)
    introcs.assert_equals([1,2,2,3,1],alist)
    
    result = lab13.removeall(alist,5)
    introcs.assert_equals([1,2,2,3,1],result)
    introcs.assert_equals([1,2,2,3,1],alist)
    
    alist = [3,3,3]
    result = lab13.removeall(alist,3)
    introcs.assert_equals([],result)
    introcs.assert_equals([3,3,3],alist)
    
    alist = [3,3,3]
    result = lab13.removeall(alist,1)
    introcs.assert_equals([3,3,3],result)
    introcs.assert_equals([3,3,3],alist)
    
    alist = [7]
    result = lab13.removeall(alist,7)
    introcs.assert_equals([],result)
    introcs.assert_equals([7],alist)
    
    alist = []
    result = lab13.removeall(alist,7)
    introcs.assert_equals([],result)
    introcs.assert_equals([],alist)


# Script code
if __name__ == '__main__':
    test_lesser_than()
    test_clamp()
    
    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_devowel()
    #test_uniques()
    #test_removeall()
    print('The modules for lab 13 passed all tests')
