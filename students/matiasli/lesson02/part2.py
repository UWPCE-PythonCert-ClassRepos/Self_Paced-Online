# to run in ipython, import this file then run part2.square_grid(x)
import math

def square_grid(size):
	rsize = math.floor(size/2)
	x =  '+' + ' -' *rsize + ' +' + ' -' *rsize + ' +'
	y = '|' + '  ' * rsize + ' |' + '  ' *rsize + ' |'
	for i1 in range(2):
		print(x)
		for i2 in range(rsize):
			print(y)
	print(x) 