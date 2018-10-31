#!/usr/bin/env python3

# task one
info = "file_{:0>3d}, {:.2f}, {:.2e}, {:.2e}"
print(info.format(2, 123.4567, 10000, 12345.67))  # this is my test statement

# task two
name = 2
first = 123.4567
second = 10000
third = 12345.67
print(f"file_{name:0>3d}, {first:.2f}, {second:.2e}, {third:.2e}")


# task three
def formatter(in_tuple):
    intro = "the {:d} numbers are : ".format(len(in_tuple))
    dec = "{:d} " * len(in_tuple)
    ans = intro + dec
    return ans.format(*in_tuple)


# task four
t4 = (4, 30, 2017, 2, 27)
print(f"{t4[3]:0>2d} {t4[4]} {t4[2]} {t4[0]:0>2d} {t4[1]}")

# task five
fruits = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {fruits[0][:-1]} is {fruits[1]}, and the weight of a {fruits[2][:-1]} is {fruits[3]}.")
print(f"The weight of an {fruits[0][:-1].upper()} is {fruits[1] * 1.2}, "
      f"and the weight of a {fruits[2][:-1].upper()} is {fruits[3] * 1.2}.")

# task six
rows = [('First', '$99.01', 'Second', '$88.09'), ('First', '$94329.01', 'Second', '$8328.09'),
        ('First', '$91249.01', 'Second', '$8328.09'), ('First', '$9439.01', 'Second', '$868.09')]
for row in rows:
    print("{:<10} {:<20} {:<10} {:<20}".format(*row))
t5 = (342, 654, 423, 789, 623, 7829, 71, 964, 1, 98)
print(("{:<5d}" * 10).format(*t5))
