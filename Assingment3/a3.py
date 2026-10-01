""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the 
stubs with your own implementations.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG. FIX IT
    return introcs.RGB(255 - rgb.red, 255 - rgb.green, 255 - rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    value = float(value)
    if round(value, 3) < 10:
        value_str = str(round(value, 3))
    elif round(value, 2) < 100:
        value_str = str(round(value, 2))
    else:
        value_str = str(round(value,1))

    if len(value_str) < 5:
        remaining = 5 - len(value_str)
        value_str += ('0' * remaining)

    return value_str


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces 
    after the commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    result = '(' + str5(cmyk.cyan) + ', ' + str5(cmyk.magenta) + ', ' + str5(cmyk.yellow) + ', ' + str5(cmyk.black) + ')'
    return result
    pass


def str5_hsl(hsl):
    """
    Returns the string representation of hsl in the form "<H, S, L>".
    
    In the output, each of H, S, and L should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsl)
    
    Example: if str(hsl) is 
    
          '<0.0,0.313725490196,0.5>'
    
    then str5_hsl(hsl) is '<0.000, 0.314, 0.500>'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsl: the color to convert to a string
    Precondition: hsl is an HSL object.
    """
    result = '<' + str5(hsl.hue) + ', ' + str5(hsl.saturation) + ', ' + str5(hsl.lightness) + '>'
    return result

    pass


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    r1 = rgb.red / 255.0
    g1 = rgb.green / 255.0
    b1 = rgb.blue / 255.0

    k = 1.0 - max(r1, g1, b1)


    if k == 1:
        return introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    c = ((1 - r1 - k) / (1 - k)) * 100
    m = ((1 - g1 - k) / (1 - k)) * 100
    y = ((1 - b1 - k) / (1 - k)) * 100
    black = k * 100.0

    return introcs.CMYK(c, m, y, black)
    
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    pass


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    c = cmyk.cyan / 100.0
    m = cmyk.magenta / 100.0
    y = cmyk.yellow / 100.0
    k = cmyk.black / 100.0

    answer = introcs.RGB(0,0,0)
    r = (1 - c) * (1 - k)
    g = (1 - m) * (1 - k)
    b = (1 - y) * (1 - k)
    r, g, b = r* 255, g * 255, b * 255
    answer.red = round(r)
    answer.blue = round(b)
    answer.green = round(g)

    return answer



    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    pass


def rgb_to_hsl(rgb):
    """
    Returns an HSL object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter rgb: the color to convert to an HSL object
    Precondition: rgb is an RGB object
    """
    r = rgb.red / 255.0
    g = rgb.green / 255.0
    b = rgb.blue / 255.0

    maximum = max(r, g, b)
    minimum = min(r, g, b)

    if maximum == minimum:
        h = 0
    elif maximum == r and g >= b:
        h = 60.0 * (g-b)/(maximum - minimum)
    elif maximum == r and g < b:
        h = 60.0 * (g-b)/(maximum - minimum) + 360.0
    elif maximum == g:
        h = 60.0 * (b-r)/(maximum - minimum) + 120.0
    elif maximum == b:
        h = 60.0 * (r-g)/(maximum - minimum) + 240.0

    l = (maximum + minimum) / 2

    if l == 0 or l == 1:
        s = 0
    else:
        s = (maximum - l)/(min(l, 1-l))

    answer = introcs.HSL(h,s,l)
    return answer
    
    
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    pass


def hsl_to_rgb(hsl):
    """
    Returns and RGB object equivalent to hsl
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsl: the color to convert to a RGB object
    Precondition: hsl is an HSL object.
    """
    h = hsl.hue
    l = hsl.lightness
    s = hsl.saturation

    hi = math.floor(h / 60)
    f = h / 60 - hi
    c = min(l, 1 - l) * s
    p = l + c
    q = l - c
    u = l - (1 - 2 * f) * c
    v = l + (1 - 2 * f) * c

    if hi == 0:
        r, g, b = p, u, q
    elif hi == 1:
        r, g, b = v, p, q
    elif hi == 2:
        r, g, b = q, p, u
    elif hi == 3:
        r, g, b = q, v, p
    elif hi == 4:
        r, g, b = u, q, p
    elif hi == 5:
        r, g, b = p, q, v

    r1 = round(r* 255.0)
    g1 = round(g* 255.0)
    b1 = round(b* 255.0)

    return introcs.RGB(r1, g1, b1)
    


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0.5, the curve is the normal line y = x, so value is 
    unaffected. If contrast < 0.5, values are pulled closer together, with all 
    values collapsing to 0.5 when contrast = 0. If contrast > 0, the values are 
    pulled farther apart, with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    m = 2 * contrast - 1 
    if contrast == 1:
        if value >= 0.5:
            y = 1
        else:
            y = 0
        return y
    if value < 0.25 + 0.25 * m:
        y = (1-m) * (value) / (1+m)
    elif value > 0.75 - 0.25 * m:
        y = (1-m) * (value - (3-m)/4) / (1+m) + ((3+m)/4)
    else: 
        y = (1+m) * (value - (1+m)/4) / (1-m) + ((1-m)/4)

    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE. It modifies rgb and has no return value. It 
    should apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    r, g, b = rgb.red / 255, rgb.green / 255, rgb.blue / 255
    r, g, b = contrast_value(r, contrast), contrast_value(g, contrast), contrast_value(b, contrast)
    r, g, b = r * 255, g * 255, b * 255
    r, g, b = round(r), round(g), round(b)
    rgb.red, rgb.green, rgb.blue = r, g, b
    

    pass
