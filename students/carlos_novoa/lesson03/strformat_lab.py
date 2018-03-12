#!/usr/bin/env python3

"""
Lesson3, String Formatting Lab Exercise
"""


def task1():
    for i, item in enumerate((2, 123.4567, 10000, 12345.67)):
        if i == 0:
            # padded number
            f = '{:0>3}'.format(item)
            r = 'file_{}'.format(f)
            _task_values.append(r)
        if i == 1:
            # floating, 2 decimals
            r = '{0:.2f}'.format(item)
            _task_values.append(r)
        if i == 2:
            # scientific notation, 2 decimals
            r = '{0:.2e}'.format(item)
            _task_values.append(r)
        if i == 3:
            # scientific notation, 3 figures
            r = '{0:3.2e}'.format(item)
            _task_values.append(r)

    # file_002 :   123.46, 1.00e+04, 1.23e+04
    print(''.join(_task_values[:1]) + ' :   ' + ', '.join(_task_values[1:]))


def task2():
    t = _task_values
    if not t:
        task1()
        task2()
        return

    # arguments
    a = t[0].split('_')[0]
    b = t[0].split('_')[1]
    c = t[1]
    d = t[2]
    e = t[3]

    # keywords
    print('{a}_{b} :   {c}, {d}, {e}'.format(a=a, b=b, c=c, d=d, e=e))

    # f-strings
    print(f'{a}_{b} :   {c}, {d}, {e}')


def task3(seq):
    sl = len(seq)
    fs = ('the {} numbers are: ' + ','.join(['{}'] * sl))
    return fs.format(sl, *seq)


def task4():
    t = (4, 30, 2017, 2, 27)
    return '{:0>2} {} {} {:0>2} {}'.format(t[3], t[4], t[2], t[0], t[1])


def task5():
    f = ['oranges', 1.3, 'lemons', 1.1]
    a, b, c, d = f[0], f[1], f[2], f[3]
    s1 = f"The weight of an {a} is {b} and the weight of a {c} is {d}"
    print(s1)
    a = a.upper()
    c = c.upper()
    s2 = f"The weight of an {a} is {b*1.2} and the weight of a {c} is {d*1.2}"
    print(s2)


def task6():
    # padded columns with alignment
    rows = [
        ['Bob', 90, '$10.00'],
        ['Joe', 23, '$100.00'],
        ['Carl', 50, '$1000.00'],
        ['Jane', 33, '$10000.00'],
    ]
    for row in rows:
        print('{0:<20}{1:^3}{2:>12}'.format(row[0], row[1], row[2]))

    # 10 columns, 5 wide
    # __1____2____3____4____5____6____7____8____9___10__
    ten = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print((''.join(['{:_^5}'] * 10)).format(*ten))


_task_values = []
