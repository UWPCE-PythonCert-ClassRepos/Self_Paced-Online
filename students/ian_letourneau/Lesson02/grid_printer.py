## Ian Letourneau
## 4/25/2018
## A script to print grids in various ways

def basic_grid():
	"""A function that prints grid exactly as shown"""
	plus, minus, slash = '+', '-', '|'
	header = plus + ' ' + (minus + ' ')*4 + plus + ' ' + (minus + ' ')*4 + plus
	body = slash + (' '*9) + slash + (' '*9) + slash
	print(header + '\n' + (body + '\n')*4 + header + '\n' + (body + '\n')*4 + header)

def print_grid(n):
	"""A function that prints a grid of n size"""
	plus, minus, slash = '+', '-', '|'
	units = int(n/2)
	header = plus + ' ' + (minus + ' ')*units + plus + ' ' + (minus + ' ')*units + plus
	if not n%2:
		body = slash + (' '*(n+1)) + slash + (' '*(n+1)) + slash
	else:
		body = slash + (' '*(n)) + slash + (' '*(n)) + slash
	print(header + '\n' + (body + '\n')*units + header + '\n' + (body + '\n')*units + header)

def print_grid2(number, size):
	"""A function that prints a grid of varioues tile size and tile number"""
	plus, minus, slash = '+', '-', '|'
	header = (plus + ' ' + (minus + ' ')*size)*number + plus
	body = (slash + (' '*(size*2+1)))*number + slash
	print((header + '\n' + (body + '\n')*size)*number + header)

