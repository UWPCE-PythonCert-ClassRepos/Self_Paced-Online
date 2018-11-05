def grid_printer():
	"""print grid as part of python 201 lesson 2"""
	print('+','-'*4,'+','-'*4,'+',sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('+','-'*4,'+','-'*4,'+',sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('|', ' '*4, '|', ' '*4, '|', sep='')
	print('+','-'*4,'+','-'*4,'+',sep='')
	
	
def print_grid(grid_size:int):
	"""defines dyamic print_grid
	args:
		n: number ofr grid elemnts verticle and horizonatal
			if odd, rounds down.  
	returns:
		na
	"""
	mark_counter = grid_size//2
	def make_border(mark_counter):
		"""helper function to make top, mid and bottom"""
		print('+','-'*mark_counter,'+','-'*mark_counter,'+',sep='')
	
	def make_middle(mark_counter):
		count = 0
		while (count<mark_counter):
			print('|', ' '*mark_counter, '|', ' '*mark_counter, '|', sep='')
			count += 1
	
	make_border(mark_counter)
	make_middle(mark_counter)
	make_border(mark_counter)
	make_middle(mark_counter)
	make_border(mark_counter)
	
def print_grid2(rows:int,elements:int, cols:int=None):
	"""defines dyamic print_grid
	args:
		rows: number of rows
		cols: number of columns
		elements: number for marks in each row/column
	returns:
		na
	"""
	# allowing for api with 2 arguments which assumes rows==cols
	if not cols:
		cols = rows
	
	def make_border(cols, elements):
		"""helper function to make top, mid and bottom"""
		col_counter = 0
		while (col_counter<cols):
			print('+','-'*elements,sep='',end='')		
			col_counter += 1
		print('+')
	
	def make_row(cols, elements):
		row_count = 0
		while (row_count<elements):
			col_counter = 0
			while (col_counter<cols):
				print('|',' '*elements,sep='',end='')
				col_counter += 1
			print('|')
			row_count += 1
	
	row_counter = 0
	while (row_counter<rows):
		make_border(cols, elements)
		make_row(cols, elements)
		row_counter += 1
	make_border(cols, elements)


