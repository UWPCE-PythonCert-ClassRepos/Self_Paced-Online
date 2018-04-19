# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 08:10:17 2018

@author: Karl M. Snyder
"""
#[[fill]align][sign][#][0][minimumwidth][.precision][type]
# use * to unpack tuple

# TASK 1
 
a_tuple = (2, 123.4567, 10000, 12345.67)
print('file_{:03}: {:.2f}, {:.2e}, {:.2e}'.format(*a_tuple))
 
# TASK 2

#by name
print('file_{num_file:03}: {_2_dec:.2f}, {_2_dec_e:.02e}, {_4digit_e:.3e}'.\
      format(num_file=2, _2_dec=123.4567, _2_dec_e=10000, _4digit_e=12345.67))
#by position
print('file_{3:03}: {0:.2f}, {1:.2e}, {1:.3e}'.format(\
      123.4567, 12345.67, 10000, 2))
#f-strings
num_file = 2
_2_dec = 123.4567
_2_dec_e = 10000
_4digit_e = 123456.67
print(f'file_{num_file:03}, {_2_dec:.2f}, {_2_dec_e:.02e}, {_4digit_e:.3e}')

# TASK 3

my_nums = (1,3,5,7,9,10,12)
def formatter(nums):
    len_nums = len(nums)
    print(('the {} numbers are: ' + ', '.join(['{}']*len_nums)).\
          format(len_nums, *nums)) 
formatter(my_nums)

# TASK 4

task4_tuple = (4, 30, 2017, 2, 27)
print('{3:02}, {4}, {2}, {0:02}, {1}'.format(*task4_tuple))

# TASK 5

my_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of the {my_list[0][:-1]} is {my_list[1]} and the \
weight of the {my_list[2][:-1]} is {my_list[3]}")


# TASK 6

rows = [['Name', 'Age', 'Cost'],
        ['Karl', 8, '$80.06'],
        ['Kate', 24, '$100.12'],
        ['Manny', 88, '$2400.99']]

for row in rows:
    print(('{:<8} {:>3}' + ' '*4 + '{:>10}').format(*row))

# EXTRA TASK
num_tuple = (20, 21, 22, 23, 24, 25, 26, 27, 28, 29)
print(' '.join(['{:5}']*len(num_tuple)).format(*num_tuple))
