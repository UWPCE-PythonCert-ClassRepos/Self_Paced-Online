"""Ian Sahlberg
Assignment 3 String Format
Python 210
12/27/2018"""

#Task One
"""( 2, 123.4567, 10000, 12345.67)

and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'"""

four = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3} : {:>8.2f}, {:.2e}, {:.3g}".format(four[0],four[1], four[2],four[3]))

#Task Two
"""Using your results from Task One, repeat the exercise, 
but this time using an alternate type of format string (hint: think about alternative ways to use .format() (keywords anyone?),
 and also consider f-strings if you’ve not used them already)."""

print(f"file_{four[0]:0>3} : {four[1]:>8.2f}, {four[2]:.2e}, {four[3]:.3g}")

#Task Three

def formatter(in_tuple):
    """Returns formatted string based on tuple length"""
    bracket_count = ", ".join(["{}"]*len(in_tuple))
    return "The " + str(len(in_tuple)) +" numbers are: " + bracket_count.format(*in_tuple)
    #print("The " + str(len(in_tuple)) + " numbers are:" + ",".join("{}"*len(in_tuple)).format(*in_tuple))



print(formatter((1,2,3,4,5)))

#Task Four

five_tup = (4, 30, 2017, 2, 27)

print(f"{five_tup[3]:0>2} {five_tup[4]} {five_tup[2]} {five_tup[0]:0>2} {five_tup[1]}")

#Task Five
"""Here’s a task for you: Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

The weight of an orange is 1.3 and the weight of a lemon is 1.1

Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher)."""

four_e = ['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {four_e[0][:-1]:} is {four_e[1]} and the weight of a {four_e[2][:-1]:} is {[four_e[3]]}')