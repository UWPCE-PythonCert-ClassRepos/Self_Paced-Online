#!/usr/bin/env python3
#string formatting

#task1
# Write a format string that will take the following four element tuple:
tuple1 = (2, 123.4567, 10000, 12345.67)
# and format it
formatted1= 'file_{0:03d}:  {1:.2f}, {2:.2e}, {3:.2e}'.format(*tuple1)
# results: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print (formatted1)

#task2 - alternate type of string formatting
print('\nTask two')
print(f'file_{tuple1[0]:03d}:  {tuple1[1]:.2f}, {tuple1[2]:.2e}, {tuple1[3]:.2e}')

#task3 - dianmically build aup format strings
def display_seq(seq):
    l=len(seq)
    print (("There are {} items, and there are: "+", ".join(["{}"]*l)).format(l,*seq))
print('\nTask three')
t = (1,2,3)
display_seq(t)

#task4 - tuple of numbers
print('\nTask four')
tuple2 = (4, 30, 2017, 2, 27)
print("{3:02d} {4} {2} {0:02d} {1}".format(*tuple2))

#task5 - f-strins example
print('\nTask five')
list1 = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {list1[0] [:-1]} is {list1[1]} and the weight\
 of a {list1[2] [:-1]} is {list1[3]}\n')

print(f'The weight of an {list1[0] [:-1].upper()} is {list1[1]*1.2} and the\
 weight of a {list1[2] [:-1].upper()} is {list1[3]*1.2}\n')

#task6 - columns
print('\nTask six')
names = ['Name1','Name11', 'Name111']
age = [5, 51, 101]
cost = [23000.50,12.00,7609.11]
for i in range(len(names)):
    print(f'{names[i]:20s} {age[i]:20n} {cost[i]:20n}')

#extra
print(' '.join(('%*s' % (5, i) for i in range(10))))
