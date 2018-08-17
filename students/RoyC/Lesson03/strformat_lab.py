#!/usr/bin/env python3
# Lesson 03, String formatting lab

# Task One
in_tuple = ( 2, 123.4567, 10000, 12345.67)
print("file_{:03d}: {:.2f}, {:.2e}, {:.2e}".format(*in_tuple))

# Task Two
print(f"file_{in_tuple[0]:03}: {in_tuple[1]:.2f}, {in_tuple[2]:.2e}, {in_tuple[3]:.2e}")

# Task Three
def formatter(in_tuple):
    """
    Return formatted string with the integer values in the given tuple
    """
    out_string = "The {:d} numbers are " + ("{:d},"*len(in_tuple))
    # print out formatted string, minus last extranneous comma
    return out_string.format(len(in_tuple), *in_tuple)[:-1]
    
print(formatter((1, 4, 2, 11, 9)))
print(formatter((5, 1, 0)))
print(formatter((3, 6, 9, 12, 15, 18)))

# Task Four
it = ( 4, 30, 2017, 2, 27)
print(f"{it[3]:02} {it[4]:02} {it[2]:04} {it[0]:02} {it[1]:02}")

# Task Five
the_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {the_list[0][:-1]} is {the_list[1]} and the weight of a {the_list[2][:-1]} is {the_list[3]}")
print(f"The weight of an {the_list[0][:-1].upper()} is {1.2*the_list[1]} and the weight of a {the_list[2][:-1].upper()} is {1.2*the_list[3]}")

# Task Six
def get_row(name, age, cost):
    """
    Return a column formatted row of data for display
    """
    return "{:<12}{:>4d}{:>10.2f}".format(name, age, cost)
    
print("{:<12}{:>4}{:>10}".format("Name", "Age", "Cost"))
print(get_row("Roy", 29, 999.99))
print(get_row("Terri", 59, 1122.50))
print(get_row("Kirby", 12, 555.25))
print(get_row("Amanda", 33, 1944.32))
print(get_row("Erin", 19, 800.21))

ten_nums = (range(995, 1005))
print(("{:<5d}"*10).format(*ten_nums))
