"""
Additional problems for more practice

This problem is taken from an old exam.  To get the proper "exam experience" you 
should complete the Vector2 functions without any method calls.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
import introcs
import math


# Vectors (You should not use any Vector2 methods)
def normalize(v):
    """
    Changes the vector v into a unit vector in the same direction.
    
    This function is a procedure.  It does not return a new vector.
    It modifies the x and y attributes of the parameter v.  If v is a
    zero vector, the function leaves it unchanged.
    
    Parameter v: the vector to normalize
    Preconditions: v is a Vector2 object
    """
    length = math.sqrt((v.x * v.x) + (v.y * v.y))
    if length > 0:
        v.x = v.x / length
        v.y = v.y / length


def project(u,v):
    """
    Returns the projection of u onto v.
    
    This function returns a new vector and does not modify either u or v.  If v is 
    the zero vector, then it returns a new zero vector.
    
    
    Parameter u: the vector to project
    Preconditions: u is a Vector2 object
    
    Parameter v: the vector to project on to
    Preconditions: v is a Vector2 object
    """
    vec = introcs.Vector2(0,0)
    if v.x == 0 and v.y == 0:
        return vec
    
    v_dot_v = (v.x * v.x + v.y * v.y)
    u_dot_v = (u.x * v.x) + (u.y * v.y)
    vec.x = (v.x * u_dot_v)/v_dot_v
    vec.y = (v.y * u_dot_v)/v_dot_v

    return vec

