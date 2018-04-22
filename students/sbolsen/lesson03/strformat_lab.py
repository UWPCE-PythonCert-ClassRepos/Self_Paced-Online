#!/usr/bin/env python3

#TASK_ONE
a = (2, 123.4567, 10000, 12345.67)
print("file_{:03d}: {:03.2f} {:0.2E} {:0.2E}".format(a[0], a[1], a[2], a[3]))

#TASK_TWO

a = (2, 123.4567, 10000, 12345.67)
print('file_{first}: {second} {third} {fourth}'.format(first = "{:03d}".format(a[0]), second = "{:03.2f}".format(a[1]), third = "{:0.2E}".format(a[2]), fourth = "{:0.2E}".format(a[3])))

#TASK_THREE

def formatter(tuple_in):
    x = tuple_in
    y = len(tuple_in)
    element = "{:d}" * y
    message = 'The {} numbers are: '.format(y)
    return message + ', '.join(str(a) for a in tuple_in)

print(formatter((25, 63, 10.4, 85, 90, 101, 345, 83.5, 12, 17)))

#TASK_FOUR

a = (4, 30, 2017, 2, 27)
print("{:02d} {} {} {:02d} {}".format(a[3], a[4], a[2], a[0], a[1]))

#TASK_FIVE

a = ['oranges', 1.3, 'lemons', 1.1]
f'The weight of an {a[0][:-1]} is {a[1]} and the weight of a {a[2][:-1]} is {a[3]}'
f'The weight of an {a[0][:-1].upper()} is {a[1] * 1.2} and the weight of a {a[2][:-1].upper()} is {a[3] *1.2}'

#TASK_SIX

values = [
        ('Dog', '5 years', '$100'),
        ('Cat', '10 years', '$25000'),
        ('Rabbit', '15 years', '$50000')
        ]
for row in values:
    print('{:10}{:12}{:12}'.format(*row))

#TASK_SIX_EXTRA

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:<5d}' * len(numbers)).format(*numbers))
