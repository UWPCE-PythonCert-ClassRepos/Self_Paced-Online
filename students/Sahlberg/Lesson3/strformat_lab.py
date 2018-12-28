"""Ian Sahlberg
Assignment 3 String Format
Python 210
12/27/2018"""


"""( 2, 123.4567, 10000, 12345.67)

and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'"""

four = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3} : {:>8.2f}, {:.2e}, {:.2e}".format(four[0],four[1], four[2],four[3]))
