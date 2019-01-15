'''
Victor A Medina
Assignment 2: Grid Printer Part 3
Purpose: Prints a grid with n_rows and with a specified size
'''
def print_grid(n_rows,size):
	plus_row='+'
	other_row='|'
	for i in range(size):
		plus_row+='-'
		other_row+=' '
	plus_row=n_rows*plus_row+'+'
	other_row=n_rows*other_row+'|'
	print(plus_row)
	for i in range(n_rows):
		for i in range(size):
			print(other_row)
		print(plus_row)