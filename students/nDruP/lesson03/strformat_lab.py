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
    prec = .2 
    return f"file_{quadruple[0]:03} :   {quadruple[1]:{prec}f}, {quadruple[2]:{prec}e}, {quadruple[3]:{prec}e}"

def disp_numbers(num_tuple):
    """
    Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    to take an arbitrary number of values.
    """
    if num_tuple:
        disp_string = "The "+str(len(num_tuple))+f" numbers are: "
        for x in range(len(num_tuple)-1):
            disp_string+="{:d}"+f"{',' if len(num_tuple)>2 else ''} "
        disp_string+="and {:d}"
        return disp_string.format(*num_tuple)
    return "There are no numbers given"

def format_quintuple(quintuple):
    """
    Take quintuple (a,b,c,d,e) and return 'd e c a b' padded w/ a zero if any of the values are single-digits
    """
    return "{:0d} {:0d} {:0d} {:0d} {:0d}".format(*quintuple)

quadruple1 = (2,123.4567,10000,12345.67)
quadruple2 = (12,3.141592654,-1234,.123456)
quadruple3 = (100,13,0,0)

assert format_quadruple(quadruple1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
assert format_quadruple(quadruple2) == 'file_012 :   3.14, -1.23e+03, 1.23e-01' 
assert format_quadruple(quadruple3) == 'file_100 :   13.00, 0.00e+00, 0.00e+00'

assert format_quadruple_alt(quadruple1) == format_quadruple(quadruple1)
assert format_quadruple_alt(quadruple2) == format_quadruple(quadruple2)
assert format_quadruple_alt(quadruple3) == format_quadruple(quadruple3)

nums0 = ()
nums2 = (8,12)
nums6 = (123,734,2346,2,666,30)

assert disp_numbers(nums0) == 'There are no numbers given'
assert disp_numbers(nums2) == 'The 2 numbers are: 8 and 12'
assert disp_numbers(nums6) == 'The 6 numbers are: 123, 734, 2346, 2, 666, and 30'

