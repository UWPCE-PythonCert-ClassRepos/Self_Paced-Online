# Task One

print('file_{0:0>3}: {1:0.2f}, {2:.2E}, {3:.2E}'.format(2, 123.4567, 10000, 12345.67))

# Task Two

one = 2
two = 123.4567
three = 10000
four = 12345.67

print(f'file_{one:0>3}: {two:0.2f}, {three:.2E}, {four:.2E}')

# Task Three


def formatter(in_tuple):
    form_string = "the " + str(len(in_tuple)) + " numbers are: " + ((len(in_tuple) - 1) * '{:d}, ') + '{:d}'
    return form_string.format(*in_tuple)

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (49, 48, 47)
print(formatter(tuple_1))
print(formatter(tuple_2))

