# print simple grid - part 3. Accept two parameters
# print_grid(3,4) = three rows, three columns and each grid cell four "units" in size

# function - print grid accepting two parameters  x == row and columns , y == units per grid
def func_print_grid(x, y):
	# loop through number of grids == x
	gridcount = 0
	while gridcount < x:
	
		# print grid line, one grid at a time, loop through variable y
		count = 0
		while count < x:
			print('+', ' - '*y, end = ' ')
			count += 1
		print('+')
		
		# print mid grid lines, one grid at a time, loop through variable y
		count = 0
		count1 = 0
		while count1 < y:
			while count < x:
				while count < x:
					print('|', ' - '*y, end = ' ')
					count += 1
				print('|')
			count1 += 1
			count = 0
		gridcount += 1
		
	# print final grid line, one grid at a time, loop through variable y
	count = 0
	while count < x:
		print('+', ' - '*y, end = ' ')
		count += 1
	print('+')
	
func_print_grid(5,4)


