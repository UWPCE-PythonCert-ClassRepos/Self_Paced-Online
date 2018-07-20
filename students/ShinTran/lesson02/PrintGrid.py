'''
Shin Tran
Python 210
Lesson 2 Assignment
'''

# Main method that print a grid, the size parameter
# is the height and length of the grid
# The grid is always four boxes
def print_grid(size):
	if (size % 2 == 1):
		half = int((size - 1) / 2)
	else:
		half = int(size / 2)
	border(half)
	for x in range(0, half):
		sides(half)
	border(half)
	for y in range(0, half):
		sides(half)
	border(half)

# Prints the border of the grid
def border(dashes):
	print ('+ ' + ('- ' * dashes) + '+ ' + ('- ' * dashes) + '+')

# Prints the side of the grid
def sides(spaces):
	print ('| ' + ('  ' * spaces) + '| ' + ('  ' * spaces) + '|')



# Main method that prints a grid based on two parameters
# First parameter, count, prints a X by X grid
# Second parameter, size, print the length and height of each box of the grid
def print_grid2(count, size):
	border = '+'
	side = '|'
	for x in range(0, count):
		for i in range(0, size):
			border +=  ' -'
		border += ' +'
	print(border)
	for y in range(0, count):
		for j in range(0, size):
			side += '  '
		side += ' |'
	for z in range(0, count):
		for k in range(0, size):
			print(side)
		print(border)
