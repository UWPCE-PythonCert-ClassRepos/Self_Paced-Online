def print_plus_sign():
	print '+', 
	
def print_dash(value):
	print '-' * value,

def print_vertical_bar(value):
	for i in range (value):
		print '|',
		print ' ' * value,
		print '|',
		print ' ' * value,
		print '|'

def print_vertical_bar2(grid_size, cell_size):
	for i in range (cell_size):
		for i in range (grid_size):
			print '|',
			print ' ' * cell_size,
		print '|'
		
def print_plus_sign_with_dash(value):
	print_plus_sign()
	print_dash(value)
	print_plus_sign()
	print_dash(value)
	print_plus_sign()
	print

def print_grid(n):
	value = n/2
	print_plus_sign_with_dash(value)
	print_vertical_bar(value)
	print_plus_sign_with_dash(value)
	print_vertical_bar(value)
	print_plus_sign_with_dash(value)

def print_plus_sign_with_dash2(grid_size, cell_size):
	for i in range(grid_size):
		print_plus_sign()
		print_dash(cell_size)
	print_plus_sign()
	print
	
def print_grid2(grid_size, cell_size):
	for i in range(grid_size):
		print_plus_sign_with_dash2(grid_size, cell_size)
		print_vertical_bar2(grid_size, cell_size)
	print_plus_sign_with_dash2(grid_size, cell_size)
	
def print_part1():
	value = 4
	print_plus_sign_with_dash(value)
	print_vertical_bar(value)
	print_plus_sign_with_dash(value)
	print_vertical_bar(value)
	print_plus_sign_with_dash(value)
	
def print_part2():
	print_grid(15)
	
def print_part3():
	print_grid2(3,4)
	print_grid2(5,3)
	
print_part1()
print_part2()
print_part3()
	
