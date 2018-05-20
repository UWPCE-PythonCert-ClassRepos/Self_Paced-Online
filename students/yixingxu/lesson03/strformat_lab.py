#!/usr/bin/env python3

# Task one
a_tuple = ( 2, 123.4567, 10000, 12345.67)
# 1 The first element is used to generate a filename that can help with file sorting.
# 2 The second element is a floating point number. You should display it with 2 decimal places shown.
# 3 The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
# 4 The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.
print('file_{:0>3d}: {:.2f}, {:.2e}, {:.3g}'.format(*a_tuple))

# Task two
# Using your results from Task One, repeat the exercise, but this time using an alternate type of format string 
#(hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already).
print(f'file_{a_tuple[0]:0>3d}: {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.3g}')

# Task Three
# Dynamically Building up Format Strings
# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values.
# Hint: You can pass in a tuple of values to a function with a *:
def formatter(in_tuple):
    l = len(in_tuple)
    form_string='the {:d} numbers are:'+'{:d},'*(l-1)+'{:d}'
    return form_string.format(l,*in_tuple)
	
if __name__ == "__main__":
	in_tuple =  (2, 123, 10000, 12345)
	formatter(in_tuple)
	another_tuple =  (2, 123)
	formatter(another_tuple)
    
# Task Four
# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'
a_tuple = ( 4, 30, 2017, 2, 27)
print('{:02d} {:d} {:d} {:02d} {:d}'.format(a_tuple[3],a_tuple[4],a_tuple[2],a_tuple[0],a_tuple[1]))

#Task Five
# Given the following four element list:
# ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1
a_list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {a_list[0]} is {a_list[1]} and the weight of a {a_list[2]} is {a_list[3]}')
# Now see if you can change the f-string so that it displays the names of the fruit in upper case, 
# and the weight 20% higher (that is 1.2 times higher).
print(f'The weight of an {a_list[0].upper()} is {a_list[1]*1.2} and the weight of a {a_list[2].upper()} is {a_list[3]*1.2}')

# Task Six
# Write some Python code to print a table of several rows, each with a name, an age and a cost. 
# Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
a_list = [['Name', 'Computer', 'Age', 10, 'Cost', '$10000'],['Name', 'Disk', 'Age', 1000, 'Cost', '$10'],['Name', 'Table','Age', 3, 'Cost', '$100']]
for item in a_list:
    print(('{:<10}'*len(item)).format(*item))
# And for an extra task, given a tuple with 10 consecutive numbers, 
# can you work how to quickly print the tuple in columns that are 5 charaters wide? It’s easily done on one short line!
a_tuple = tuple(range(1,11))
print(('{:<5}'*len(a_tuple)).format(*a_tuple))    

input("Close.") # keep python open until closing

    
    