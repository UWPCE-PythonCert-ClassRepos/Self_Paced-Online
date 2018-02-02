#!/usr/bin/env python3

def format_quadruple(quadruple):
    """
    The first element is used to generate a filename that can help with file sorting.
    The second element is a floating point number. You should display it with 2 decimal places shown.
    The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
    The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.
    """
    return "file_{0[0]:03} :   {0[1]:.2f}, {0[2]:.2e}, {0[3]:.2e}".format(quadruple)

def format_quadruple_alt(quadruple):
    """
    Use an alternate type of format string to replicate results of format_quadruple. (keywords/f-strings)
    """
    return f"file_{file_num:03} :   {floats_2dec:.2f}, {int_sci_2dec:.2e}, {float_sci_3sig:.2e}"

quadruple1 = (2,123.4567,10000,12345.67)
quadruple2 = (12,3.141592654,-1234,.123456)
quadruple3 = (100,13,0,0)

assert format_quadruple(quadruple1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
assert format_quadruple(quadruple2) == 'file_012 :   3.14, -1.23e+03, 1.23e-01' 
assert format_quadruple(quadruple3) == 'file_100 :   13.00, 0.00e+00, 0.00e+00'

assert format_quadruple_alt(quadruple1) == format_quadruple(quadruple1)
assert format_quadruple_alt(quadruple2) == format_quadruple(quadruple2)
assert format_quadruple_alt(quadruple3) == format_quadruple(quadruple3)
