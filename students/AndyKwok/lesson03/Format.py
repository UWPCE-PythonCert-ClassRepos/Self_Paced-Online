# Description: 
# Author: Andy Kwok
# Last Updated: 07/10/2018
# ChangeLog: 
#   v1.0 - Initialization

#test tuple
test = ( 2, 123.4567, 10000, 12345.67)



#Task One
print('Task One - format()')
print('file_{:04d}, {:.2f}, {:.2e}, {:.3e}'.format(test[0], test[1], test[2], test[3]))

#Task Two
print('Task Two - f-strings')
print(f'file_{test[0]:04d}, {test[1]:.2f}, {test[2]:.2e}, {test[3]:.3e}')

#Task Three
print('Task Three - Dynamic Tuple')
length = len(test)
form_string = '{}, '*(length-1) + '{}'
print('The {} numbers are '.format(length) + form_string.format(*test))

def formatter(in_tuple):
    """ Function to print the list of numbers and the quantity
    in_tuple: input tuple
    """
    length = len(in_tuple)
    form_string = '{}, '*(length-1) + '{}'
    return 'The {} numbers are '.format(length) + form_string.format(*in_tuple)

#Task Four
print('Task Four - Tuple Reordering')
date = (4, 30, 2017, 2, 27)
print (('{:02d} {:02d} {:04d} {:02d} {:02d}').format(date[3], date[4], date[2], date[0], date[1]))


#Task Five
print('Task Five - f-strings')
string = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {string[0].upper()} is {string[1]*1.2} and the weight of a {string[2].upper()} is {string[3]*1.2}')

#Task Six
print('Task Six - Alignment')
title = ('Name', 'Cost', 'Age')
num1 = ('Caleb', 10.001, 50)
num2 = ('Kristen', 10.02, 99)
num3 = ('Jack', 10.3, 5)
print (('{:10} {:<7} {:<10}').format(*title))
print (('{:10} {:<7} {:<10}').format(*num1))
print (('{:10} {:<7} {:<10}').format(*num2))
print (('{:10} {:<7} {:<10}').format(*num3))

num_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Extra Task:')
for id in num_list: print('{:0>5}'.format(id))