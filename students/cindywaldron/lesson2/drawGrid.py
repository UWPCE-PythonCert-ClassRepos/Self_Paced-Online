def printGrid(x,y):
	"""
	Description: printGrid prints grids with given cell size
	and grid size.                                   
	:param: x - cell size
	:param: y - grid size
	"""
	for i in range(x):
		# construct string with pattern of '+', ' ', and '-'
		str = y*(' ' + '-') + ' '
		# construct one row of string based on cell size
		outerRow = x*( '+' + str) + '+'
		print(outerRow)
		
		for j in range(y):
			#construct string with pattern of ' '
			str = 2*y*(' ') + ' '
			#construct one row of string with pattern '|', ' ', and '|'
			innerRow = x*('|' + str ) + '|'
			print(innerRow)
	print(outerRow)