"""
A module with one more turtle shape

This module consists of two functions to be implemented. 

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
from introcs.turtle import Window, Turtle, Pen
import introcs  # For the RGB (color) objects
import math     # For the math computations

#################### Lab Functions ####################

# THIS IS ALREADY COMPLETED FOR YOU
def color_poly(w, radius, n, sp):
    """
    Draws a colored polygon using color_poly_helper(t, radius, n, sp)
    
    This function clears the window and makes a new turtle t. This turtle starts 
    in the middle of the canvas facing the default east. It then calls the 
    function color_poly_helper(t, side, ang, n, sp). When it is done, the turtle 
    is left VISIBLE.
    
    REMEMBER: You need to flush the turtle if the speed is 0.
    
    This procedure asserts all preconditions.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter radius: The polygon radius
    Precondition: radius is a valid  length (number >= 0)
    
    Parameter n: The number of edges of the polygon
    Precondition: n is a valid number of iterations (int >= 1)
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_window(w)
    assert is_valid_length(radius)
    assert is_valid_iteration(n)
    assert is_valid_speed(sp)
    
    w.clear()
    
    t = Turtle(w)
    t.visible = True
    color_poly_helper(t,radius,n,sp)
    
    t.flush()


# WORK ON THIS FUNCTION
def color_poly_helper(t, radius, n, sp):
    """
    Draws an n-sided regular colored polygon with the given radius.
    
    The polygon will centered at the current turtle position. The first vertex 
    of the polygon will be radius units along the current turtle heading. 
    
    This function is similar to draw_polygon from a4.py. It moves forward by
    radius amount without drawing. It uses an angle of 360.0/n to turn 
    90+angle/2 degrees left, orienting it on the polygon. It draws n lines
    of length 2*pi*sin(pi/n) length, turning angle left each time. When done, 
    it returns to its original position. It does this by turning 90+angle/2 
    degrees right and moving backwards by radius amount.
    
    The ONLY differences between this function and draw_polygon are (1) the
    parameter sp, (2) precondtions are enforced, and (3) the color of the 
    turtle. In particular, at each step, the the color of the turtle should be 
    alternate between "red", "blue", "magenta", and "cyan", starting at "red"
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED: 
    position (x and y, within round-off errors), heading, color, speed, visible, 
    and drawmode. There is no need to restore these.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter radius: The polygon radius
    Precondition: radius is a valid side length (number >= 0)
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(radius), report_error('radius is not a valid length', radius)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)

    original_color = t.color
    original_speed = t.speed
    original_drawmode = t.drawmode
    original_header = t.header

    angle = 360.0/n
    side = 2*radius*math.sin(math.pi/n)

    t.speed = sp
    t.drawmode = False
    t.forward(radius)
    t.left(90+angle/2)
    t.drawmode = original_drawmode

    colors = ['red', 'blue', 'magenta', 'cyan']
    for i in range(n):
        t.color = colors[i % 4]
        t.forward(side)
        t.left(angle)

    t.drawmode = False
    t.right(90+angle/2)
    t.backward(radius)
    t.drawmode = original_drawmode
    t.color = original_color
    t.speed = original_speed
    t.header = original_header


################ Helpers for Precondition Verification #################

def is_number(x):
    """
    Returns: True if value x is a number; False otherwise.
    
    Parameter x: the value to check
    Precondition: NONE (x can be any value)
    """
    return type(x) in [float, int]


def is_window(w):
    """
    Returns: True if w is a introcs Window; False otherwise.
    
    Parameter w: the value to check
    Precondition: NONE (w can be any value)
    """
    return type(w) == Window


def is_valid_color(c):
    """
    Returns: True c is a valid turtle color; False otherwise
    
    Parameter c: the value to check
    Precondition: NONE (c can be any value)
    """
    if type(c) == str:
        return introcs.is_tkcolor(c) or introcs.is_webcolor(c)
    # else
    return type(c) == introcs.RGB or type(c) == introcs.HSV


def is_valid_speed(sp):
    """
    Returns: True if sp is an int in range 0..10; False otherwise.
    
    Parameter sp: the value to check
    Precondition: NONE (sp can be any value)
    """
    return (type(sp) == int and 0 <= sp and sp <= 10)


def is_valid_length(side):
    """
    Returns: True if side is a number >= 0; False otherwise.
    
    Parameter side: the value to check
    Precondition: NONE (side can be any value)
    """
    return (is_number(side) and 0 <= side)


def is_valid_iteration(n):
    """
    Returns: True if n is an int >= 1; False otherwise.
    
    Parameter n: the value to check
    Precondition: NONE (n can be any value)
    """
    return (type(n) == int and 1 <= n)


def is_valid_depth(d):
    """
    Returns: True if d is an int >= 0; False otherwise.
    
    Parameter d: the value to check
    Precondition: NONE (d can be any value)
    """
    return (type(d) == int and d >= 0)


def is_valid_turtlemode(t):
    """
    Returns: True t is a Turtle with drawmode True; False otherwise.
    
    Parameter t: the value to check
    Precondition: NONE (t can be any value)
    """
    return (type(t) == Turtle and t.drawmode)


def is_valid_penmode(p):
    """
    Returns: True t is a Pen with solid False; False otherwise.
    
    Parameter p: the value to check
    Precondition: NONE (p can be any value)
    """
    return (type(p) == Pen and not p.solid)


def report_error(message, value):
    """
    Returns: An error message about the given value.
    
    This is a function for constructing error messages to be used in assert 
    statements. We find that students often introduce bugs into their assert 
    statement messages, and do not find them because they are in the habit of 
    not writing tests that violate preconditions.
    
    The purpose of this function is to give you an easy way of making error 
    messages without having to worry about introducing such bugs. Look at  the 
    function draw_two_lines for the proper way to use it.
    
    Parameter message: The error message to display
    Precondition: message is a string
    
    Parameter value: The value that caused the error
    Precondition: NONE (value can be anything)
    """
    return message+': '+repr(value)
