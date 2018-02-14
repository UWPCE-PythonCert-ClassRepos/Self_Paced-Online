#!/usr/bin/env python3

# Task 1

values = (2, 123.4567, 10000, 12345.67)
formatter = 'file_{:03d}: {:05.2f}, {:.2E}, {:.2E}'
output = formatter.format(*values)

print(output)

# Task 2

formatter2 = 'file_{a[0]:03d}: {a[1]:05.2f}, {a[2]:.2E}, {a[3]:.2E}'
output2 = formatter2.format(a=values)

output3 = f'file_{values[0]:03d}: {values[1]:05.2f}, {values[2]:.2E}, {values[3]:.2E}'

print(output2)
print(output3)

# Task 3


def dynamic_format(seq):
    l = len(seq)
    return (('The {} numbers are: ' + ", ".join(['{}']*l)).format(l, *seq))

print(dynamic_format(values))

# Task 4

tup = (4, 30, 2017, 2, 27)

print(f"{tup[3]:02d} {tup[4]:02d} {tup[2]:02d} {tup[0]:02d} {tup[1]:02d}")

# Task 5

given = ['oranges', 1.3, 'lemons', 1.1]
display = f"The weight of an {given[0][:-1]} is {given[1]} and the weight of a {given[2][:-1]} is {given[3]}"
display2 = f"The weight of an {given[0][:-1].upper()} is {given[1]*1.2} and the weight of a {given[2][:-1].upper()} is {given[3]*1.2}"

print(display)
print(display2)

# Task 6

cars = [("Ferrari", 90000, 2), ("Mercedes", 17000, 6), ("Unknown", 100, 17), ("Pinto", 5, 30), ("BMW", 9000, 10)]
for car in cars:
    print("{:10} ${:7,} {:6} years old".format(*car))

consec = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
consec2 = []
for x in consec:
    consec2.append(x*500)

print(("{:5}" * 10).format(*consec))
print(("{:5}" * 10).format(*consec2))
