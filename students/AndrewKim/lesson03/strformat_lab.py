#Task 1

a_tuple = (2, 123.4567, 10000, 12345.67)

print(f'file_{a_tuple[0]:03d} :  {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}')

#Task 2

print("file_{0:03d} :  {1:.2f}, {2:.2e}, {3:.2e}".format(a_tuple[0], a_tuple[1], a_tuple[2], a_tuple[3]))

#Task 3

b_tuple = ( 3, 4, 5, 6)

print("the 3 numbers are: {:d}, {:d}, {:d}".format(*b_tuple))

#Task 4

c_tuple = ( 4, 30, 2017, 2, 27)

print("'{} {} {} {} {}'".format(c_tuple[3], c_tuple[4], c_tuple[2], c_tuple[0], c_tuple[1]))

#Task 5

list1 = ['oranges', 1.3, 'lemons', 1.1]

print(f"The weight of an {list1[0][:-1]} is {list1[1]} and the weight of a {list1[2][:-1]} is {list1[3]}")

print(f"The weight of an {list1[0][:-1].upper()} is {list1[1]*1.2} and the weight of a {list1[2][:-1].upper()} is {list1[3]*1.2}")

#Task 6

names = ['Andrew', 'Jamie', 'Annie', 'Caroline', 'Billy']
age = [31, 28, 26, 30, 32]
cost = [340.11, 290.07, 445.67, 99.10, 2390.19]

print("Name       |Age    |Cost")
for i in range(5):
    print('{:<11}|{:<7}|{}'.format(names[i], age[i], cost[i]))