# collection of functions to print grids by Alejandro Guardia


def print_grid_std():
# prints a standard grid, takes no argument
	joint = "+"
	row_marks =" - "
	colum_marks="|"
	print(joint+row_marks*4+joint+row_marks*4+joint)
	print()
	for i in range(4):
	    print(colum_marks+" "*12+colum_marks+" "*12+colum_marks)
	    print()
	print(joint+row_marks*4+joint+row_marks*4+joint)
	print()
	for i in range(4):
	    print(colum_marks+" "*12+colum_marks+" "*12+colum_marks)
	    print()
	print(joint+row_marks*4+joint+row_marks*4+joint)
	
print_grid_std()
      