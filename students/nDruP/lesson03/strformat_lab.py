#!/usr/bin/env python3


def format_quadruple(file_num, float_2dec, sci_int, sci_3float):
    """
    The first element is used to generate a filename that can help with file sorting.
    The second element is a floating point number. You should display it with 2 decimal places shown.
    The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
    The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.
    """
    return "file_{:03} :   {:.2f}, {:.2e}, {:.2e}".format(file_num, float_2dec, sci_int, sci_3float)


assert format_quadruple(2,123.4567,10000,12345.67) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
assert format_quadruple(12,3.141592654,-1234,.123456) == 'file_012 :   3.14, -1.23e+03, 1.23e-01' 
assert format_quadruple(100,13,0,0) == 'file_100 :   13.00, 0.00e+00, 0.00e+00'
