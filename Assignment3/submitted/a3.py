"""
Functions for Assignment A3
This file contains the functions for the assignment.
Names: Joon Lee (jl4875) + Richard Li (rl998)
Date: October 1, 2026
"""
import introcs
import math

def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    result = introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)
    return result


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
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    decimal_value = float(value)
    if decimal_value >= 100:
        rounded_value = round(decimal_value, 1)
    elif decimal_value >= 10:
        rounded_value = round(decimal_value, 2)
    else:
        rounded_value = round(decimal_value, 3)
    text = str(rounded_value)
    text_length = len(text)
    if text_length == 3:
        text = text+'00'
    elif text_length == 4:
        text = text+'0'
    return text


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk).
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is a CMYK object.
    """
    cyan_value = cmyk.cyan
    magenta_value = cmyk.magenta
    yellow_value = cmyk.yellow
    black_value = cmyk.black
    cyan_text = str5(cyan_value)
    magenta_text = str5(magenta_value)
    yellow_text = str5(yellow_value)
    black_text = str5(black_value)
    result = ('(' + cyan_text + ', ' + magenta_text + ', ' +
          yellow_text + ', ' + black_text + ')')
    return result


def str5_hsl(hsl):
    """
    Returns the string representation of hsl in the form "(H, S, L)".
    In the output, each of H, S, and L should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsl).
    Parameter hsl: the color to convert to a string
    Precondition: hsl is an HSL object.
    """
    hue_value = hsl.hue
    saturation_value = hsl.saturation
    lightness_value = hsl.lightness
    hue_text = str5(hue_value)
    saturation_text = str5(saturation_value)
    lightness_text = str5(lightness_value)

    result = ('(' + hue_text + ', ' + saturation_text + ', ' +
          lightness_text + ')')

    return result


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    red_value = rgb.red
    green_value = rgb.green
    blue_value = rgb.blue

    red_fraction = red_value/255.0
    green_fraction = green_value/255.0
    blue_fraction = blue_value/255.0

    largest_rgb_fraction = max(red_fraction,
                               green_fraction,
                               blue_fraction)

    black_fraction = 1.0-largest_rgb_fraction

    if black_fraction == 1.0:
        cyan_fraction = 0.0
        magenta_fraction = 0.0
        yellow_fraction = 0.0
    else:
        denominator = 1.0-black_fraction

        cyan_fraction = (1.0-red_fraction-black_fraction)/denominator
        magenta_fraction = (1.0-green_fraction-black_fraction)/denominator
        yellow_fraction = (1.0-blue_fraction-black_fraction)/denominator

    cyan_percent = cyan_fraction*100.0
    magenta_percent = magenta_fraction*100.0
    yellow_percent = yellow_fraction*100.0
    black_percent = black_fraction*100.0

    result = introcs.CMYK(cyan_percent,
                          magenta_percent,
                          yellow_percent,
                          black_percent)
    return result


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk.

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to an RGB object
    Precondition: cmyk is a CMYK object.
    """
    cyan_percent = cmyk.cyan
    magenta_percent = cmyk.magenta
    yellow_percent = cmyk.yellow
    black_percent = cmyk.black

    cyan_fraction = cyan_percent/100.0
    magenta_fraction = magenta_percent/100.0
    yellow_fraction = yellow_percent/100.0
    black_fraction = black_percent/100.0

    remaining_after_black = 1.0-black_fraction
    red_fraction = (1.0-cyan_fraction)*remaining_after_black
    green_fraction = (1.0-magenta_fraction)*remaining_after_black
    blue_fraction = (1.0-yellow_fraction)*remaining_after_black

    red_scaled = red_fraction*255.0
    green_scaled = green_fraction*255.0
    blue_scaled = blue_fraction*255.0

    red_value = round(red_scaled)
    green_value = round(green_scaled)
    blue_value = round(blue_scaled)

    result = introcs.RGB(red_value,
                         green_value,
                         blue_value)
    return result


def rgb_to_hsl(rgb):
    """
    Returns an HSL object equivalent to rgb.

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter rgb: the color to convert to an HSL object
    Precondition: rgb is an RGB object
    """
    red_value = rgb.red
    green_value = rgb.green
    blue_value = rgb.blue

    red_fraction = red_value/255.0
    green_fraction = green_value/255.0
    blue_fraction = blue_value/255.0

    maximum_fraction = max(red_fraction,
                           green_fraction,
                           blue_fraction)
    minimum_fraction = min(red_fraction,
                           green_fraction,
                           blue_fraction)

    difference = maximum_fraction-minimum_fraction

    if difference == 0:
        hue = 0.0
    elif maximum_fraction == red_fraction and green_fraction >= blue_fraction:
        green_minus_blue = green_fraction-blue_fraction
        hue_ratio = green_minus_blue/difference
        hue = 60.0*hue_ratio
    elif maximum_fraction == red_fraction and green_fraction < blue_fraction:
        green_minus_blue = green_fraction-blue_fraction
        hue_ratio = green_minus_blue/difference
        hue_piece = 60.0*hue_ratio
        hue = hue_piece+360.0
    elif maximum_fraction == green_fraction:
        blue_minus_red = blue_fraction-red_fraction
        hue_ratio = blue_minus_red/difference
        hue_piece = 60.0*hue_ratio
        hue = hue_piece+120.0
    else:
        red_minus_green = red_fraction-green_fraction
        hue_ratio = red_minus_green/difference
        hue_piece = 60.0*hue_ratio
        hue = hue_piece+240.0

    lightness = (maximum_fraction+minimum_fraction)/2.0

    if lightness == 0.0 or lightness == 1.0:
        saturation = 0.0
    else:
        saturation_denominator = min(lightness, 1.0-lightness)
        saturation = (maximum_fraction-lightness)/saturation_denominator

    hue = float(hue)
    saturation = float(saturation)
    lightness = float(lightness)

    result = introcs.HSL(hue,
                         saturation,
                         lightness)
    return result


def hsl_to_rgb(hsl):
    """
    Returns an RGB object equivalent to hsl.

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsl: the color to convert to an RGB object
    Precondition: hsl is an HSL object.
    """
    hue = hsl.hue
    saturation = hsl.saturation
    lightness = hsl.lightness

    hue_divided_by_sixty = hue/60.0
    hue_index = math.floor(hue_divided_by_sixty)

    hue_fraction = hue_divided_by_sixty-hue_index

    smaller_lightness_side = min(lightness, 1.0-lightness)
    chroma = smaller_lightness_side*saturation

    positive_value = lightness+chroma
    negative_value = lightness-chroma

    hue_offset = (1.0-2.0*hue_fraction)*chroma

    lower_middle_value = lightness-hue_offset
    upper_middle_value = lightness+hue_offset

    if hue_index == 0:
        red_fraction = positive_value
        green_fraction = lower_middle_value
        blue_fraction = negative_value
    elif hue_index == 1:
        red_fraction = upper_middle_value
        green_fraction = positive_value
        blue_fraction = negative_value
    elif hue_index == 2:
        red_fraction = negative_value
        green_fraction = positive_value
        blue_fraction = lower_middle_value
    elif hue_index == 3:
        red_fraction = negative_value
        green_fraction = upper_middle_value
        blue_fraction = positive_value
    elif hue_index == 4:
        red_fraction = lower_middle_value
        green_fraction = negative_value
        blue_fraction = positive_value
    else:
        red_fraction = positive_value
        green_fraction = negative_value
        blue_fraction = upper_middle_value

    red_scaled = red_fraction*255.0
    green_scaled = green_fraction*255.0
    blue_scaled = blue_fraction*255.0

    red_value = round(red_scaled)
    green_value = round(green_scaled)
    blue_value = round(blue_scaled)

    result = introcs.RGB(red_value,
                         green_value,
                         blue_value)
    return result


def contrast_value(value, contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast.

    At contrast = 0.5, the curve is the normal line y = x, so value is
    unaffected. If contrast < 0.5, values are pulled closer together, with all
    values collapsing to 0.5 when contrast = 0. If contrast > 0.5, the values
    are pulled farther apart, with all values becoming 0 or 1 when contrast = 1.

    Parameter value: the value to adjust
    Precondition: value is a float in 0..1

    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    if contrast == 1.0:
        if value >= 0.5:
            result = 1.0
        else:
            result = 0.0
        return result

    slope_parameter = 2.0*contrast-1.0
    lower_boundary = 0.25+0.25*slope_parameter
    upper_boundary = 0.75-0.25*slope_parameter

    if value < lower_boundary:
        outer_slope = (1.0-slope_parameter)/(1.0+slope_parameter)

        result = outer_slope*value
    elif value > upper_boundary:
        outer_slope = (1.0-slope_parameter)/(1.0+slope_parameter)

        right_shift = (3.0-slope_parameter)/4.0
        shifted_value = value-right_shift

        scaled_shifted_value = outer_slope*shifted_value

        right_height = (3.0+slope_parameter)/4.0

        result = scaled_shifted_value+right_height
    else:
        middle_slope = (1.0+slope_parameter)/(1.0-slope_parameter)

        middle_shift = (1.0+slope_parameter)/4.0
        shifted_value = value-middle_shift

        scaled_shifted_value = middle_slope*shifted_value

        middle_height = (1.0-slope_parameter)/4.0

        result = scaled_shifted_value+middle_height

    return result


def contrast_rgb(rgb, contrast):
    """
    Applies the given contrast to the RGB object rgb.

    This function is a PROCEDURE. It modifies rgb and has no return value. It
    should apply contrast_value to the red, blue, and green values.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    original_red = rgb.red
    original_green = rgb.green
    original_blue = rgb.blue

    red_fraction = original_red/255.0
    green_fraction = original_green/255.0
    blue_fraction = original_blue/255.0

    contrasted_red_fraction = contrast_value(red_fraction,
                                              contrast)
    contrasted_green_fraction = contrast_value(green_fraction,
                                                contrast)
    contrasted_blue_fraction = contrast_value(blue_fraction,
                                               contrast)

    new_red = round(contrasted_red_fraction*255.0)
    new_green = round(contrasted_green_fraction*255.0)
    new_blue = round(contrasted_blue_fraction*255.0)

    rgb.red = new_red
    rgb.green = new_green
    rgb.blue = new_blue