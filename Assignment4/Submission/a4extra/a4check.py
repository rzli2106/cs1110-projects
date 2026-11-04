"""
Test script for the A4 extras

This test script is exactly like a4test.py, except that it is used to test the
new function in a4extra.

Author: Walker M. White (wmw2)
Date: Oct 13, 2025
"""
import a4extra
import introcs
from introcs.turtle import Window, Turtle, Pen


#################### Task 3A: Spirals ####################

def test_color_poly(w,sp):
    """
    Tests the procedure color_poly AND draw_color_poly
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the 
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    print('Testing color_poly  (n=8)')
    # This is only ONE TEST. Feel free to change the values for different tests.
    
    # First verify that the preconditions are enforced
    introcs.assert_error(a4extra.color_poly,'window',120,8,sp)
    introcs.assert_error(a4extra.color_poly,w,'120',8,sp)
    introcs.assert_error(a4extra.color_poly,w,-1,8,sp)
    introcs.assert_error(a4extra.color_poly,w,120,"8",sp)
    introcs.assert_error(a4extra.color_poly,w,120,-1, sp)
    introcs.assert_error(a4extra.color_poly,w,120,8,str(sp))
    introcs.assert_error(a4extra.color_poly,w,120,8,-1)
    introcs.assert_error(a4extra.color_poly,w,120,8,9.5)
    
    # Now draw
    a4extra.color_poly(w, 120, 8, sp)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')

    print('Testing color_poly (n=64)')
    a4extra.color_poly(w, 200, 64, sp)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')
    
    print('Testing color_poly_helper')
    # This is only ONE TEST. Feel free to change the values for different tests.
    w.clear()
    turt = Turtle(w)
    
    # First verify that the preconditions are enforced
    turt.drawmode = False
    introcs.assert_error(a4extra.color_poly_helper,turt,250,360,sp)
    turt.drawmode = True
    introcs.assert_error(a4extra.color_poly_helper,turt,'250',360,sp)
    introcs.assert_error(a4extra.color_poly_helper,turt,-1,360,sp)
    introcs.assert_error(a4extra.color_poly_helper,turt,-1,'360',sp)
    introcs.assert_error(a4extra.color_poly_helper,turt,250,-1,sp)
    introcs.assert_error(a4extra.color_poly_helper,turt,250,20.5,sp)
    introcs.assert_error(a4extra.color_poly_helper,turt,250,360,str(sp))
    introcs.assert_error(a4extra.color_poly_helper,turt,250,360,-1)
    introcs.assert_error(a4extra.color_poly_helper,turt,250,360,9.5)
    
    # Store original values (These are all of the important ones)
    oldcol  = turt.color
    oldvis  = turt.visible
    oldspd  = turt.speed
    oldmode = turt.drawmode
    
    # Now draw
    a4extra.color_poly_helper(turt, 250, 360, sp)
    
    # Verify value restored
    introcs.assert_equals(oldcol, turt.color)
    introcs.assert_equals(oldvis,turt.visible)
    introcs.assert_equals(oldspd,turt.speed)
    introcs.assert_equals(oldmode,turt.drawmode)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### Main Test Procedure ####################

def get_speed():
    """
    Returns the answer to a prompt about the speed.
    
    If the anwser is invalid, it returns the value 10
    """
    ans = input('Enter the drawing speed [0..10]: ')
    try:
        return int(ans.strip())
    except:
        print('Answer '+repr(ans)+' is invalid. Using speed 10.')
        return 10


def test_all():
    """
    Tests all of the drawing functions in a4extra.
    
    This is the master test procedure.  It creates a drawing window and sets the 
    drawing speed for all of the tests.
    
    If you want to disable a test (because the turtle is not very fast, and so you 
    do not want to keep drawing the same things), comment it out in the code below.
    """
    print('Testing module a4extra')
    w  = Window()
    sp = get_speed()
    
    # Test procedures. 
    test_color_poly(w,sp)
    
    print('Testing complete')


if __name__ == '__main__':
    test_all()