#!/usr/bin/env python3

#Lesson 03: String Formatting
#Natalie Rodriguez
#3/16/2018

#Tuple to Use
tup = (2, 123.4567, 10000, 12345.67)

#Task 1
#Print the first item so that it is padded with zeros.
# Make the second element, a float, to display with 2 decimal places shown.
#Display item three, an integer, in scientific notation, with 2 decimal places shown.
# Make the fourth element, a float, to display in scientific notation with 3 significant figures.

def task1():
    print(f"file_{tup[0]:03d}: {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.2e}")

task1()

#Task 2
# Do the same as above using alternative methods.

def task2():
    print("file_{0:03d}: {1:.2f}, {2:.2e}, {3:.2e}".format(tup[0], tup[1], tup[2], tup[3]))

task2()

#Task 3
# Build a dynamic format string with any input
# that prints "The {} numbers are: {}, {}, {}, etc...

def task3(*tuple):
    tuple_length = len(tuple)
    format_string = '{:d},' * (tuple_length - 1) + '{:d}'
    return "The {} numbers are: ".format(tuple_length) + format_string.format(*tuple)

#Task 4
#Given (4, 30, 2017, 2, 27)
#Print ' 02 27 2017 04 30'
#Use indexing.

t_four = (4, 30, 2017, 2, 27)

def task4():
    template = '{0:02d} {1:d} {2:d} {3:02d} {4:d}'
    return template.format(t_four[3], t_four[4], t_four[2], t_four[0], t_four[1])

#Task 5
# Given list ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string to display:
# The weight of an orange is 1.3 and
#the weight weight of a lemon is 1.1.

task_list = ['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {task_list[0][:6]} is {task_list[1]} and the weight of a {task_list[2][:5]} is {task_list[3]}.')

print(f'The weight of an {task_list[0][:6].upper()} is {task_list[1]*1.2} and the weight of a {task_list[2][:5].upper()} is {task_list[3]*1.2}.')

#Task 6
#Print a table with columns titled, name, age and cost.
#Format it so that everything aligns nicely.

dogs = [('NAME', 'AGE', 'COST'), ('Virgil', 6, '$763,867.23'), ('River', 5, '$127,543.43'),
        ('Kibson', 1, '$8,573.95'), ('Dexter', 11, '$835.67'),
        ('China', 3, '$354.99'), ('Lucy', 7, '$231.58'), ('Percy', 4, '$1.99'),]


for idx, item in enumerate(dogs):
    print('{:<10} {:<5} {:<10}'.format(dogs[idx][0], dogs[idx][1], dogs[idx][2]))

numbers = range(100, 110)
print(("{:5}" * 10).format(*numbers))