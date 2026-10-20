"""

A module with an additional color function

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def warmup(color1,color2):
    """
    MODIFIES color1 to be closer to color2

    This function compares each (non-alpha) attribute of color1 and color2.
    If the color1 attribute is larger, nothing happens. Otherwise, it adds
    10 to the color1 attribute (making sure not to violate RGB invariants).

    Parameter color1: The color to modify
    Precondition: color1 is an RGB object

    Parameter color2: The color to compare
    Precondition: color2 is an RGB object
    """
    if color2.red > color1.red and color1.red + 10 <= 255:
        color1.red += 10
    elif color2.red > color1.red and color1.red + 10 > 255:
        color1.red = 255

    if color2.green > color1.green and color1.green + 10 <= 255:
        color1.green += 10
    elif color2.green > color1.green and color1.green + 10 > 255:
        color1.green = 255

    if color2.blue > color1.blue and color1.blue + 10 <= 255:
        color1.blue += 10
    elif color2.blue > color1.blue and color1.blue + 10 > 255:
        color1.blue = 255
