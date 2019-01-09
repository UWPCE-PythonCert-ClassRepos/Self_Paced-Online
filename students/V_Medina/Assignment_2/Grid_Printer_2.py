'''
Victor A Medina
Assignment 2: Grid Printer Part 2
'''
def print_grid(n):
	plus_row=''
	for i in range(n):
		if i%2==0:
			plus_row+=' '
		else:
			plus_row+='-'
	col_length=len(plus_row)
	plus_row="+"+plus_row+"+"+plus_row+"+"
	other_row="|"+' '*col_length+"|"+' '*col_length+"|"
	print(plus_row)
	for i in range(plus_row.count('-')-1):
			print(other_row,)
	print(plus_row)
	for i in range(plus_row.count('-')-1):
			print(other_row,)
	print(plus_row)