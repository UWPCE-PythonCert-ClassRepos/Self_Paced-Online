#!/usr/bin/env python3

# Task 1
t = (2, 123.4567, 10000, 12345.67)
s = "file_{:03}: {:.2f}, {:.2e}, {:.2e}".format(*t)
print(s)

# Task 2
print(f"file_{t[0]:03}: {t[1]:.2f}, {t[2]:.2e}, {t[3]:.2e}")

# Task 3
def formatter(in_tuple):
    size = len(in_tuple)
    format_string = "The {} numbers are: {}" + (",  {}" * (size - 1))
    return format_string.format(size, *in_tuple)

print(formatter((1, 3, 56, 88, 4, 55, 7)))

# Task 4
t = (4, 30, 2017, 2, 27)
print(f"{t[3]:02} {t[4]:02} {t[2]:02} {t[0]:02} {t[1]:02}")

# Task 5
l = ["oranges", 1.3, "lemons", 1.1]
print(f"The weight of an {l[0][:-1]} is {l[1]} and the weight of a {l[2][:-1]} is {l[3]}")
print(f"The weight of an {l[0][:-1].upper()} is {l[1] * 1.2} and the weight of a {l[2][:-1].upper()} is {l[3] * 1.2}")

# Task 6
def print_row(name, age, cost):
    print("{:<10}{:>5}{:>10.2f}".format(name, age, cost))

print("{:<10}{:>5}{:>10}".format("Name", "Age", "Cost"))
print("-"*25)
print_row("Steven", 55, 345.66)
print_row("Hal", 3, 5326.00)
print_row("Heather", 27, 54.33)
print_row("Bill", 101, 12354.38)

t = (range(999,1010))
print(("{:<5}"*10).format(*t))