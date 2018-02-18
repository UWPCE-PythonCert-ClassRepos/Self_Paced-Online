#!/usr/bin/env python3

# task one
x = (2, 123.4567, 10000, 12345.67)
print('file{:03d}: {:0.2f} {:0.2E} {:0.2E}'.format(x[0], x[1], x[2], x[3]))

# task two
print('file{:03d}: {:0.2f} {:0.2E} {:0.2E}'.format(*x))

# task three
length = len(x)
new_x = 'the {} numbers are: '.format(length) + ', '.join(['{}'] * length).format(*x)
print(new_x)

# task four '02 27 2017 04 30'
y = (4, 30, 2017, 2, 27)
print('{:02d} {} {} {:02d} {}'.format(y[3], y[-1], y[2], y[0], y[1]))

# task five
data = ['oranges', 1.3, 'lemons', 1.1]
data_out1 = f"The weight of an {data[0][:-1]} is {data[1]} and the weight of a {data[2][:-1]} is {data[3]}"
data_out2 = f"The weight of an {data[0][:-1].upper()} is {data[1]*1.2} and the weight of a {data[2][:-1].upper()} is {data[3]*1.2}"

print(data_out1)
print(data_out2)

# task six
buildings = [("Building1", 90000000, 25), ("Building2", 33000000, 34),
        ("Building3", 120000000, 23)]
for bldg in buildings:
    print("{:12} ${:8,} {:3} years old".format(*bldg))

nums = range(100, 110)
print(("{:5}" * 10).format(*nums))