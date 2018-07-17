#!/usr/bin/env python3

a_tuple = (2, 123.4567, 10000, 12345.67)

print("file{:03d}: {:.2f}, {:.2e}, {:.2e}".format(*a_tuple))

#part 2: using f string
print(f"file{a_tuple[0]:03d}, {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}")

#part 3
def formatter(in_tuple):
    form_string = ("the {:d} numbers are: " + ("{}, " *(len(in_tuple) - 1)) + "{}").format(len(in_tuple), *in_tuple)
    return form_string

print(formatter(a_tuple))

#part 4
b_tuple = (4,30,2017,2,27)
print(f"{b_tuple[3]:02d} {b_tuple[4]:d} {b_tuple[2]:d} {b_tuple[0]:02d} {b_tuple[1]:d}")

#part 5
a_list = ['oranges', 1.3, 'lemons',1.1]

print(f"The weight of an {a_list[0]} is {a_list[1]} and the weight of a {a_list[2]} is {a_list[3]}")

print(f"The weight of an {a_list[0].upper()} is {a_list[1]*1.2} and the weight of a {a_list[2].upper()} is {a_list[3]*1.2}")

#part 6

rows = [['Fred', '45', '$99.45'],['Mary', '60', '$190.99'],['John', '56', '$2345.99']]

for row in rows:
    print('{:20}{:10}{:>8}'.format(*row))