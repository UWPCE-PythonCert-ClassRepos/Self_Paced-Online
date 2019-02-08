#!/usr/bin/env python3

# Task one
elements = (2, 123.4567, 10000, 12345.67)
print("file_{}: {}, {:.2e}, {:.2e}".format(str(elements[0]).zfill(3), elements[1].__round__(2), elements[2], elements[3]))

# Task two
results = ("file_002:", 123.46, 1.00e+04, 1.23e+04)
print(f"{results[0]} {results[1]}, {results[2]:.2e}, {results[3]:.2e}")

# Task three
def task_three(tuple):
    length = len(tuple)
    numbers = "{:d}, " * (length - 1) + "{:d}"
    return("the {} numbers are: ".format(length) + numbers.format(*tuple))

print(task_three((2,3,4)))
print(task_three((2,3,5,7,9)))

# Task four
four = (4, 30, 2017, 2, 27)
print("{:0>2d} {} {} {:0>2d} {}".format(four[3], four[4], four[2], four[0], four[1]))

# Task five
five = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {five[0][:-1]} is {five[1]} and the weight of a {five[2][:-1]} is {five[3]}")
print(f"The weight of an {five[0][:-1].upper()} is {five[1] * 1.2} and the weight of a {five[2][:-1].upper()} is {five[3] * 1.2}")

# Task six
column_names = ("Name", "Age", "Cost")
data = (("Matt", "30", "1000"), ("Gina", "29", "50000"), ("Dakota", "7", "700"))
print("{:^10} {:^10} {:^10}".format(*column_names))
for row in data:
    print("{:<10} {:^10} ${:<10}".format(*row))