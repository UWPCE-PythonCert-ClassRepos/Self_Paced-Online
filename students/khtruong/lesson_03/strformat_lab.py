#!/usr/bin/env python

"""Sample module docstrings text
"""


def task1():
    """Return a formatted string for each element in tuple.

    Write a format string that will take the following four element tuple:
    ( 2, 123.4567, 10000, 12345.67)
    and produce:
    'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """
    t = (2, 123.4567, 10000, 12345.67)
    strformat = 'file_{:0>3d} :{:9.2f}, {:.2e}, {:.3g}'.format(*t)
    return strformat


def task2():
    """Return a formatted string same as task1 but using a different method."""
    t = (2, 123.4567, 10000, 12345.67)
    t0 = '%03d' % (t[0])
    t1 = '% 9.2f' % (t[1])
    t2 = '%.2e' % (t[2])
    t3 = '%.3g' % (t[3])
    strformat = 'file_{} :{}, {}, {}'.format(t0, t1, t2, t3)
    return strformat


def task3(t):
    """Return a formatted string for a tuple of any length.

    Dynamically Rewrite: the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    """
    strformat = ''.join(['the ', '{:d} ', 'numbers are: ',
                         ', '.join(['{:d}'] * len(t))
                         ]
                        )
    return strformat.format(len(t), *t)


def task4():
    """Return a formatted 5 element tuple.

    Given a 5 element tuple:
    (4, 30, 2017, 2, 27)
    use string formating to print:
    '02 27 2017 04 30'
    Hint: use index numbers to specify positions.
    """
    t = (4, 30, 2017, 2, 27)
    strformat = '{3:0>2d}, {4:d}, {2:d}, {0:0>2d}, {1:d}'.format(*t)
    return strformat


def task5():
    """Return a formatted string using f-string.

    Here’s a task for you: Given the following four element list:
    ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display:
    The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Now see if you can change the f-string so that it displays the names
    of the fruit in upper case, and the weight 20% higher
    (that is 1.2 times higher).
    """
    l = ['oranges', 1.3, 'lemons', 1.1]
    fruit1 = l[0]
    weight1 = l[1]
    fruit2 = l[2]
    weight2 = l[3]
    strformat = f'the weight of an {fruit1[:-1]} is {weight1} ' \
                f'and the weight of a {fruit2[:-1]} is {weight2}'
    strformat2 = f'the weight of an {fruit1[:-1].upper()} is {1.2*weight1} ' \
                 f'and the weight of a {fruit2[:-1].upper()} is {1.2*weight2}'
    return strformat, strformat2


def task6():
    """Return a table using alignment seperator.

    Write some Python code to print a table of several rows,
    each with a name, an age and a cost. Make sure some of the
    costs are in the hundreds and thousands to test your alignment specifiers.
    """
    l = [['Superman', 29, 10000],
         ['Wonder Woman', 5000, 1000],
         ['Spiderman', 15, 100]]
    for row in l:
        print('{:>{width}s} {:>{width}d} {:>{width}d}'.format(*row, width=15))


def task6bonus():
    """Return a column of 10 consecutive numbers.

    And for an extra task, given a tuple with 10 consecutive numbers, can you
    work how to quickly print the tuple in columns that are 5 charaters wide?
    It’s easily done on one short line!
    """
    t = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    [print('{:5}'.format(item)) for item in t]

print(task1())
print(task2())
print(task3((1, 2, 3, 4)))
print(task4())
print(task5())
task6()
task6bonus()
