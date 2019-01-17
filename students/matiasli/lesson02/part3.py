# third part of UW python homework 2
# function that draws a square grid with a specified number size and units
# print_grid2(3,4)  three rows, three columns, and each grid cell four “units” in size

def print_grid2(size, units):
	x = '+'
	y = '|'
	for j1 in range(size):
		x = x + ' -' * units + ' +'
		y = y + '  ' * units + ' |'

	for i1 in range(size):
		print(x)
		for i2 in range(units):
			print(y)
	print(x) 