#!/usr/bin/env python3
"""
Victor Medina
1/12/2019
Lesson 3: String Formatting
"""


# Task1
def generate_file_name(seq):
    return 'file_{:0>3d}: {:.2f},{:.2e},{:.2e}'.format(*seq)


# Task2
def generate_file_name_f_string(seq):
    filename = seq[0]
    values = seq[1:]
    return f"file_{filename}: {values[0]},{values[1]},{values[2]}"


# Task3
def formatter(seq):
    l = len(seq)
    return ('the {} numbers are ' + ', '.join(["{}"] * l)).format(l, *seq)


# Task4
seq4 = (4, 30, 2017, 2, 27)
print('{:0>2d} {:0>2d} {:0>2d} {:0>2d} {:0>2d}'.format(seq4[3], seq4[4], seq4[2], seq4[0], seq4[1]))

# Task5
elements = ['oranges', 1.3, 'lemons', 1.1]
Str1 = f"The weight of an {elements[0]} is {elements[1]} and the weight of a {elements[2]} is {elements[3]}"
Str2 = f"The weight of an {elements[0].upper()} is {elements[1] * 1.2} and the weight of a {elements[2].upper()} is " \
    f"{elements[3] * 1.2}"
print(Str1)
print(Str2)

# Task6
rows = [
    ['Bob', '12', '$88.09'],
    ['Matt', '27', '$8.09'],
    ['Jose', '6', '$188.09'],
    ['Michelle', '62', '$1288.09'],
    ['Dylan', '9', '$10288.09']
]

for row in rows:
    print('{:<10}{:>10}{:>12s}'.format(*row))

# Task6 Bonus
conseq_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = len(conseq_seq)
print(''.join(["{:5}"] * l).format(*conseq_seq))
