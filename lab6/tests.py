"""
A test script to test the module funcs.py

Richard Li
Sept 10 2026
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing
import quotes

# TEST PROCEDURE
def test_asserts():
    """
    This is a simple test procedure to help you understand how assert works
    """
    print('Testing the introcs asserts')
    introcs.assert_equals('b c', 'ab cd'[1:4])
    #introcs.assert_equals('b c', 'ab cd'[1:3])     # UNCOMMENT ONLY WHEN DIRECTED

    introcs.assert_true(3 < 4)
    introcs.assert_equals(3, 1+2)

    introcs.assert_equals(3.0, 1.0+2.0)
    #introcs.assert_equals(6.3, 3.1+3.2)            # UNCOMMENT ONLY WHEN DIRECTED

def test_has_a_vowel():
    """
    This is a simple test procedure to help you understand how has_a_vowel works
    """
    print('Testing function has_a_vowel')
    result = funcs.has_a_vowel('aeiou')
    introcs.assert_equals(True, result)

def test_first_inside_quotes():
    """
    This is a simple test procedure to help you understand how first_inside_quotes works
    """
    print('Testing function first_inside_quotes')
    result = quotes.first_inside_quotes('"A"BCD')
    introcs.assert_equals('A', result)

    result = quotes.first_inside_quotes('ABCD""')
    introcs.assert_equals('', result)

    result = quotes.first_inside_quotes('"abc""def"')
    introcs.assert_equals('abc', result)

    result = quotes.first_inside_quotes('"asdf"')
    introcs.assert_equals('asdf', result)

def test_replace_first():
    """
    This is a simple test procedure to help you understand how replace_first works
    """
    print('Testing function replace_first')
    result = funcs.replace_first('crane','a','o')
    introcs.assert_equals('crone', result)




# SCRIPT CODE (Call Test Procedures here)
test_asserts()
test_has_a_vowel()
test_first_inside_quotes()
test_replace_first()
print('Module funcs is working correctly')
