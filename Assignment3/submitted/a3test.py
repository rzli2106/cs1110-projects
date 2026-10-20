"""

Unit Test for Assignment A3
This module implements several test cases for a3. It is incomplete. You should
look though this file for places to add tests.
Names: Joon Lee (jl4875) + Richard Li (rl998)
Date: October 1, 2026
"""
import introcs
import a3

def test_complement():
    """
    Test function complement
    """
    print('Testing complement')

    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)

    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)

def test_str5():
    """
    Test function str5
    """
    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('0.000',  a3.str5(1e-9))
    introcs.assert_equals('0.000',  a3.str5(0))
    introcs.assert_equals('1.000',  a3.str5(1))
    introcs.assert_equals('10.00',  a3.str5(10))
    introcs.assert_equals('99.00',  a3.str5(99))
    introcs.assert_equals('360.0',  a3.str5(360))

def test_str5_color():
    """
    Test the str5 functions for cmyk and hsl.
    """
    print('Testing str5_cmyk and str5_hsl')

    # Tests for str5_cmyk

    # Mixed CMYK values with different digit lengths
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)

    # CMYK minimum, maximum, and decimal values
    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)

    # CMYK values that round across digit boundaries
    text = a3.str5_cmyk(introcs.CMYK(9.9999, 10.0, 99.995, 100.0))
    introcs.assert_equals('(10.00, 10.00, 100.0, 100.0)',text)

    # Tests for str5_hsl

    # HSL zero hue with ordinary saturation and lightness
    text = a3.str5_hsl(introcs.HSL(0.0, 0.313725, 0.5))
    introcs.assert_equals('(0.000, 0.314, 0.500)',text)

    # HSL hue near maximum with full saturation
    text = a3.str5_hsl(introcs.HSL(359.94, 1.0, 0.0456))
    introcs.assert_equals('(359.9, 1.000, 0.046)',text)

    # HSL zero saturation and maximum lightness
    text = a3.str5_hsl(introcs.HSL(72.846, 0.0, 1.0))
    introcs.assert_equals('(72.85, 0.000, 1.000)',text)

    # HSL values rounding across ten and to endpoints
    text = a3.str5_hsl(introcs.HSL(9.9999, 0.9999, 0.0004))
    introcs.assert_equals('(10.00, 1.000, 0.000)',text)

    # HSL hue rounding across one hundred
    text = a3.str5_hsl(introcs.HSL(99.995, 0.12345, 0.98765))
    introcs.assert_equals('(100.0, 0.123, 0.988)',text)

def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')

    # The function should guarantee accuracy to three decimal places

    # White RGB boundary
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    # Black RGB
    rgb = introcs.RGB(0, 0, 0)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))

    # Mixed RGB values
    rgb = introcs.RGB(217, 43, 164)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))

def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    # No ink gives white
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)

    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Maximum black gives black
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Pure cyan
    cmyk = introcs.CMYK(100.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Pure magenta
    cmyk = introcs.CMYK(0.0, 100.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Pure yellow
    cmyk = introcs.CMYK(0.0, 0.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Magenta and yellow produce red
    cmyk = introcs.CMYK(0.0, 100.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Cyan and yellow produce green
    cmyk = introcs.CMYK(100.0, 0.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Cyan and magenta produce blue
    cmyk = introcs.CMYK(100.0, 100.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Maximum CMY without black
    cmyk = introcs.CMYK(100.0, 100.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Partial black only
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 50.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    # Half cyan tests rounding
    cmyk = introcs.CMYK(50.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)

    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Half magenta tests rounding
    cmyk = introcs.CMYK(0.0, 50.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Half yellow tests rounding
    cmyk = introcs.CMYK(0.0, 0.0, 50.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    # Mixed values from RGB conversion
    cmyk = introcs.CMYK(0.0, 80.184, 24.424, 14.902)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(217, rgb.red)
    introcs.assert_equals(43, rgb.green)
    introcs.assert_equals(164, rgb.blue)

    # Mixed CMYK values with partial black
    cmyk = introcs.CMYK(20.0, 40.0, 60.0, 20.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(163, rgb.red)
    introcs.assert_equals(122, rgb.green)
    introcs.assert_equals(82, rgb.blue)

    # Fractional CMYK percentages
    cmyk = introcs.CMYK(33.3, 66.6, 12.5, 17.5)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(140, rgb.red)
    introcs.assert_equals(70, rgb.green)
    introcs.assert_equals(184, rgb.blue)

def test_rgb_to_hsl():
    """
    Test translation function rgb_to_hsl
    """
    print('Testing rgb_to_hsl')

    # Black achromatic boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(0, 0, 0))
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(0.0, round(hsl.lightness,3))

    # White achromatic boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(255, 255, 255))
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(1.0, round(hsl.lightness,3))

    # Mid-gray achromatic value
    hsl = a3.rgb_to_hsl(introcs.RGB(128, 128, 128))
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(0.502, round(hsl.lightness,3))

    # Red hue boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(255, 0, 0))
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Yellow hue boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(255, 255, 0))

    introcs.assert_equals(60.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Green hue boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(0, 255, 0))
    introcs.assert_equals(120.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Cyan hue boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(0, 255, 255))
    introcs.assert_equals(180.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Blue hue boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(0, 0, 255))
    introcs.assert_equals(240.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Magenta hue boundary
    hsl = a3.rgb_to_hsl(introcs.RGB(255, 0, 255))
    introcs.assert_equals(300.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Red-max hue with green above blue
    hsl = a3.rgb_to_hsl(introcs.RGB(255, 128, 0))
    introcs.assert_equals(30.118, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Red-max hue with green below blue
    hsl = a3.rgb_to_hsl(introcs.RGB(255, 0, 128))
    introcs.assert_equals(329.882, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Green-max interior hue
    hsl = a3.rgb_to_hsl(introcs.RGB(0, 255, 128))
    introcs.assert_equals(150.118, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Blue-max interior hue
    hsl = a3.rgb_to_hsl(introcs.RGB(128, 0, 255))
    introcs.assert_equals(270.118, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Dark mixed color
    hsl = a3.rgb_to_hsl(introcs.RGB(100, 50, 25))
    introcs.assert_equals(20.0, round(hsl.hue,3))
    introcs.assert_equals(0.6, round(hsl.saturation,3))
    introcs.assert_equals(0.245, round(hsl.lightness,3))

    # Light mixed color
    hsl = a3.rgb_to_hsl(introcs.RGB(230, 180, 150))
    introcs.assert_equals(22.5, round(hsl.hue,3))
    introcs.assert_equals(0.615, round(hsl.saturation,3))
    introcs.assert_equals(0.745, round(hsl.lightness,3))

    # Nearly gray low-saturation color
    hsl = a3.rgb_to_hsl(introcs.RGB(127, 128, 128))
    introcs.assert_equals(180.0, round(hsl.hue,3))
    introcs.assert_equals(0.004, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    # Nearly black saturated color
    hsl = a3.rgb_to_hsl(introcs.RGB(1, 0, 0))

    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.002, round(hsl.lightness,3))

    # Nearly white saturated color
    hsl = a3.rgb_to_hsl(introcs.RGB(254, 255, 255))
    introcs.assert_equals(180.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.998, round(hsl.lightness,3))

def test_hsl_to_rgb():
    """
    Test translation function hsl_to_rgb
    """
    print('Testing hsl_to_rgb')

    # Hue sector 0 boundary
    rgb = a3.hsl_to_rgb(introcs.HSL(0.0, 1.0, 0.5))
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Hue sector 1 boundary
    rgb = a3.hsl_to_rgb(introcs.HSL(60.0, 1.0, 0.5))
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Hue sector 2 boundary
    rgb = a3.hsl_to_rgb(introcs.HSL(120.0, 1.0, 0.5))
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Hue sector 3 boundary
    rgb = a3.hsl_to_rgb(introcs.HSL(180.0, 1.0, 0.5))
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Hue sector 4 boundary
    rgb = a3.hsl_to_rgb(introcs.HSL(240.0, 1.0, 0.5))
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Hue sector 5 boundary
    rgb = a3.hsl_to_rgb(introcs.HSL(300.0, 1.0, 0.5))
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Interior of hue sector 0
    rgb = a3.hsl_to_rgb(introcs.HSL(30.0, 0.5, 0.25))
    introcs.assert_equals(96, rgb.red)
    introcs.assert_equals(64, rgb.green)
    introcs.assert_equals(32, rgb.blue)

    # Interior of hue sector 1
    rgb = a3.hsl_to_rgb(introcs.HSL(90.0, 0.5, 0.25))
    introcs.assert_equals(64, rgb.red)
    introcs.assert_equals(96, rgb.green)
    introcs.assert_equals(32, rgb.blue)

    # Interior of hue sector 2
    rgb = a3.hsl_to_rgb(introcs.HSL(150.0, 0.5, 0.25))
    introcs.assert_equals(32, rgb.red)
    introcs.assert_equals(96, rgb.green)
    introcs.assert_equals(64, rgb.blue)

    # Interior of hue sector 3
    rgb = a3.hsl_to_rgb(introcs.HSL(210.0, 0.5, 0.25))

    introcs.assert_equals(32, rgb.red)
    introcs.assert_equals(64, rgb.green)
    introcs.assert_equals(96, rgb.blue)

    # Interior of hue sector 4
    rgb = a3.hsl_to_rgb(introcs.HSL(270.0, 0.5, 0.25))
    introcs.assert_equals(64, rgb.red)
    introcs.assert_equals(32, rgb.green)
    introcs.assert_equals(96, rgb.blue)

    # Interior of hue sector 5
    rgb = a3.hsl_to_rgb(introcs.HSL(330.0, 0.5, 0.25))
    introcs.assert_equals(96, rgb.red)
    introcs.assert_equals(32, rgb.green)
    introcs.assert_equals(64, rgb.blue)

    # Hue near upper boundary
    rgb = a3.hsl_to_rgb(introcs.HSL(359.0, 1.0, 0.5))
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(4, rgb.blue)

    # Zero saturation gives gray
    rgb = a3.hsl_to_rgb(introcs.HSL(200.0, 0.0, 0.5))
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    # Minimum lightness gives black
    rgb = a3.hsl_to_rgb(introcs.HSL(0.0, 1.0, 0.0))
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # Maximum lightness gives white
    rgb = a3.hsl_to_rgb(introcs.HSL(0.0, 1.0, 1.0))
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # Light color in first hue sector
    rgb = a3.hsl_to_rgb(introcs.HSL(30.0, 0.5, 0.75))
    introcs.assert_equals(223, rgb.red)
    introcs.assert_equals(191, rgb.green)
    introcs.assert_equals(159, rgb.blue)

    # Light color in fourth hue sector
    rgb = a3.hsl_to_rgb(introcs.HSL(210.0, 0.5, 0.75))
    introcs.assert_equals(159, rgb.red)
    introcs.assert_equals(191, rgb.green)
    introcs.assert_equals(223, rgb.blue)

def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')

    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0,0.0)
    introcs.assert_floats_equal(0.5,result)

    # Other endpoint at minimum contrast
    result = a3.contrast_value(1.0,0.0)
    introcs.assert_floats_equal(0.5,result)

    # contrast < 0.5, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.25)
    introcs.assert_floats_equal(0.3,result)

    # contrast < 0.5, middle of sawtooth
    result = a3.contrast_value(0.4,0.3)
    introcs.assert_floats_equal(0.4571429,result)

    # contrast < 0.5, upper part of sawtooth
    result = a3.contrast_value(0.9,0.35)
    introcs.assert_floats_equal(0.8142857,result)

    # contrast == 0.5, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.5)
    introcs.assert_floats_equal(0.1,result)

    # contrast == 0.5, middle of sawtooth
    result = a3.contrast_value(0.6,0.5)
    introcs.assert_floats_equal(0.6,result)

    # contrast == 0.5, middle part of sawtooth
    result = a3.contrast_value(0.9,0.5)
    introcs.assert_floats_equal(0.9,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.1,0.65)
    introcs.assert_floats_equal(0.05384615,result)

    # contrast > 0, upper of sawtooth
    result = a3.contrast_value(0.4,0.75)
    introcs.assert_floats_equal(0.2,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.7)
    introcs.assert_floats_equal(0.95714286,result)

    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2,1.0)
    introcs.assert_floats_equal(0.0,result)

    # Upper half at maximum contrast
    result = a3.contrast_value(0.6,1.0)
    introcs.assert_floats_equal(1.0,result)

def test_contrast_rgb():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_rgb')

    # Darkening (less than 0.5) contrast
    rgb = introcs.RGB(240, 15, 118)
    a3.contrast_rgb(rgb,0.3)
    introcs.assert_equals(220, rgb.red)
    introcs.assert_equals(35,  rgb.green)
    introcs.assert_equals(123, rgb.blue)

    # Minimum contrast
    rgb = introcs.RGB(0, 128, 255)
    a3.contrast_rgb(rgb,0.0)
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    # Neutral contrast
    rgb = introcs.RGB(25, 128, 230)
    a3.contrast_rgb(rgb,0.5)
    introcs.assert_equals(25, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(230, rgb.blue)

    # Contrast above 0.5
    rgb = introcs.RGB(32, 128, 224)
    a3.contrast_rgb(rgb,0.75)
    introcs.assert_equals(11, rgb.red)
    introcs.assert_equals(129, rgb.green)
    introcs.assert_equals(245, rgb.blue)

    # Maximum contrast
    rgb = introcs.RGB(40, 128, 220)
    a3.contrast_rgb(rgb,1.0)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

# Script code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsl()
    test_hsl_to_rgb()
    test_contrast_value()
    test_contrast_rgb()
    print('Module a3 passed all tests.')

# omg this took so long 😭