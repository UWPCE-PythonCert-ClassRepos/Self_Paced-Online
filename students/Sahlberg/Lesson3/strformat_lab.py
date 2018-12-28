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

print(f'The weight of an {four_e[0][:-1].upper()} is {four_e[1]*1.2} and the weight of a {four_e[2][:-1].upper()} is {four_e[3]*1.2}')

#Task 6
"""Then you will need to use alignment specifiers. Do some research on this using the links below. Then:

Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of 
the costs are in the hundreds and thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple 
in columns that are 5 charaters wide? It’s easily done on one short line!"""

profile = [['Bob', '26', '126.00'],['JuanitaClaritaMansanita', '5', '126,000,000'], ['Ronathan', '75', '100,000'], ['Sir Marcus the 3rd','33', '33']]

for file in profile:
    print('{:<20}{:<10}{:<8}'.format(*file))

