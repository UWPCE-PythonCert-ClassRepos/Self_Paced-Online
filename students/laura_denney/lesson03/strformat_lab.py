#-------------------------------------------------#
# Title: String Formatting
# Dev:   LDenney
# Date:  October 10, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/10/18, Created File
#-------------------------------------------------#

#task 1------------------------------------------
tupl =  (2, 123.4567, 10000, 12345.67)
str = "file_{:03d}:  {:.2f}, {:.2e}, {:3.2e}".format(*tupl)
print(str)

#task 2------------------------------------------
str2 = f"file_{tupl[0]:03d}:  {tupl[1]:.2f}, {tupl[2]:.2e}, {tupl[3]:3.2e}"
print(str2)

#task 3------------------------------------------

def formatter(in_tuple):
    leng = len(in_tuple)
    fstring = "the {:d} numbers are: " + ", ".join(["{:d}"] * leng)
    return fstring.format(leng, *in_tuple)

#task 4------------------------------------------

#task 5------------------------------------------

#task 6------------------------------------------


