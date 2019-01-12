# second part of UW python homework 2. creates a square of user specified size, rounding down
# to run in ipython, import this file then run part2.print_grid(x)
import math

def print_grid(size):
	rsize = math.floor(size/2)
	x =  '+' + ' -' *rsize + ' +' + ' -' *rsize + ' +'
	y = '|' + '  ' * rsize + ' |' + '  ' *rsize + ' |'
	for i1 in range(2):
		print(x)
		for i2 in range(rsize):
			print(y)
	print(x) 