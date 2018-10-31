def print_grid():
	gridrow =2
	gd = 4 # number of spaces between plus signs
	plus = '+'
	minus = '-'
	vbar = "|"
	space = " "

	line = plus + (minus * gd) + plus + (minus* gd) + plus
	line2 = vbar + (space * gd) + vbar + (space * gd) + vbar


	for i in range(gridrow):
		print(line)
		for i in range(gd):
			print(line2) 
	print(line)


