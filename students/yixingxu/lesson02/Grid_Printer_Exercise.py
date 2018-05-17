def print_grid(x):
	if type(x) != int or x<3:
		print('input needs to be an integer and >= 3')
		return
	plus = '+'
	minus = '-'
	space = ' '
	vertical_line = '|'
	cell_length = x//2
	cell_per_side = 2
	 
	horizontal = cell_per_side*(plus + ' '  + cell_length*(minus+space))+plus
	vertical = cell_per_side*(vertical_line +  ' '  + cell_length*(2*space))+vertical_line

	for i in range(cell_per_side):
		print(horizontal)
		for i in range(cell_length):
			print(vertical)
			
	print(horizontal)
	
def print_grid2(x,y):
	if type(x) != int or x<1:
		print('number of cells needs to be an integer and >= 1')		
		return
	if type(y) != int or y<1:
		print('units of cells length needs to be an integer and >= 1')		
		return
	plus = '+'
	minus = '-'
	space = ' '
	vertical_line = '|'
	cell_length = y
	cell_per_side = x
	 
	horizontal = cell_per_side*(plus + ' '  + cell_length*(minus+space))+plus
	vertical = cell_per_side*(vertical_line +  ' '  + cell_length*(2*space))+vertical_line

	for i in range(cell_per_side):
		print(horizontal)
		for i in range(cell_length):
			print(vertical)
			
	print(horizontal)	
	
if __name__ == '__main__' :
	x= 3
	print_grid(x)
	
	rows = 3
	cell_units = 4
	print_grid2(rows,cell_units)
	
	
