#!/usr/bin/env python3
__author__ = "Wieslaw Pucilowski"

# Task One
print('{:*^100}'.format(' Task One '))
tup = ( 2, 123.4567, 10000, 12345.67)
#'file_002 :   123.46, 1.00e+04, 1.23e+04'

print("file_{:0>3} : {:.2f}, {:.2e}, {:.2e}".format(tup[0], tup[1], tup[2], tup[3]))

# Task Two
print('{:*^100}'.format(' Task Two '))
print(f'file_{tup[0]:0>3} : {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.2e}')

# Task Three
print('{:*^100}'.format(' Task Three '))
first=(1,2,3,4,5,6)
second=(1,2,3,4,5,6,7,8,9,10)
def formatter(tup):
	l=len(tup)
	out_str=("the {:d} numbers are: "+", ".join(["{:d}"]*(l))).format(l, *tup)
	return out_str

print(formatter(first))
print(formatter(second))

# Task Four
print('{:*^100}'.format(' Task Four '))
tup = ( 4, 30, 2017, 2, 27) # to '02 27 2017 04 30'
print("{3:02d} {4} {2} {0:02d} {1}".format(*tup))
# print("{3:0>2} {4} {2} {0:0>2} {1}".format(*tup))

# Task Five
print('{:*^100}'.format(' Task Five '))
fruits = ['oranges', 1.3, 'lemons', 1.1]
# The weight of an orange is 1.3 and the weight of a lemon is 1.1
# The weight of an {fruits[0]} is {fruits[1]} and the weight of a {fruits[2]}  is {fruits[3]}

print(f'The weight of an {fruits[0]} is {fruits[1]} and the weight of a {fruits[2]}  is {fruits[3]}')
print("The weight 20% higher:")
print(f'The weight of an {fruits[0].upper()} is {fruits[1]*1.2} and the weight of a {fruits[2].upper()}  is {fruits[3]*1.2}')

# Task Six
print('{:*^100}'.format(' Task Six '))

# ex. 'First $99.01 Second $88.09'
table = [('First', '$99.01', 'Second', '$88.09'),
		 ('First', '$9999999.01', 'Second', '$8888.09'),
		 ('First', '$9.01', 'Second', '$888888.09'),
		 ('First', '$999999.01', 'Second', '$8.09'),
		]
		
for row in table:
	print(("".join(["{:<20}"]*len(row))).format(*row))

print()


print('{:*^100}'.format(' TABLE: NAME, AGE, COST '))

columns = ['Name:', 'Age:', 'Cost:']	
names = [('Bob', '28', '$88.09'),
		 ('Kyle', '39', '$8888.09'),
		 ('Matt', '47', '$888888.09'),
		 ('Jim', '23', '$8.09'),
		 ('Suzan', '31', '$8.09')]
		
print(("".join(["{:<20}"]*len(columns))).format(*columns))
for row in names:
	print(("".join(["{:<20}"]*len(row))).format(*row))
	
print('{:*^100}'.format(' EXTRA '))

tup=(1,2,3,4,5,6,7,8,9,10)

def print_tup(tup):
    print(("".join(["{:<5}"]*len(tup))).format(*tup))

print_tup(tup)
