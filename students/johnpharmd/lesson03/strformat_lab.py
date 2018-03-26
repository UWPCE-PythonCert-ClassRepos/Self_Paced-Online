#!/usr/bin/env python3

# started with form_st = 'file_{:d}: {:f}, {:d}, {:f}'
# Internet search pointed me to https://docs.python.org/2/library/string.html,
# which, apparently, is not (completely) deprecated in Python 3.
# Also used https://docs.python.org/3.3/library/string.html#formatstrings.
# iteration: form_st = 'file_{:03d}: {:f}, {:e}, {:e}'
# iteration: form_st = 'file_{:03d}: {:.2f}, {:e}, {:e}'
# iteration: form_st = 'file_{:03d}: {:.2f}, {:.2e}, {:e}'
# Task 1
 form_st = 'file_{:03d}: {:.2f}, {:.2e}, {:.2e}'

 # Task 2
 # started with:
 # form_st2 = 'file_{integer}: {flo}, {expo1}, {expo2}'
 # Found this:
 # https://stackoverflow.com/questions/3228865/how-do-i-format-a-number-with-a-variable-number-of-digits-in-python
 form_st1 = 'file_{num:0{width}}: {flo:.2f}, {expo1:.2e}, {expo2:.2e}'


# Task 3
# Rewrite 'the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)' to
# take an arbitrary number of values.

# form_string = 'the {} numbers are:...'
# see Chris B's video at 5:10 in
def formatter(in_tuple):
    l = len(in_tuple)
    output0 = 'the {} numbers are: '
    output1 = ', '.join(['{}'] * l)
    return (output0 + output1).format(l, *in_tuple)


# Task 4
"""
Given a 5 element tuple:

    (4, 30, 2017, 2, 27)

    use string formating to print:

    '02 27 2017 04 30'

Hint: use index numbers to specify positions.
"""
def task4(in_tuple):
    i_t = in_tuple
    form_string = ' '.join(['{:02d} ']) * 4 + '{:02d}'
    return form_string.format(i_t[3], i_t[4], i_t[2], i_t[0], i_t[1])


# Task 5
"""
Given the following four element list:

    ['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

    The weight of an orange is 1.3 and the weight of a lemon is 1.1
"""
fw = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an', fw[0][:-1], 'is', fw[1],
	'and the weight of a', fw[2][:-1], 'is', fw[3])

# Change the f-string so that it displays the names of the fruit in
# upper case, and the weight 20% higher (that is 1.2 times higher).
print(f'The weight of an', fw[0][:-1].upper(), 'is', fw[1] * 1.2,
	'and the weight of a', fw[2][:-1].upper(), 'is', fw[3] * 1.2)


# Task 6
