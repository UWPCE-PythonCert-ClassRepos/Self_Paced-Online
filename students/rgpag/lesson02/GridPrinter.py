
#the chars selected for these vars can be modified to create more fun grids :)
space_plus = ' +'
space_dash = ' -'
space_pipe = ' |'
space_space = "  "

#Part1 fixed size 2x2 grid
def print_grid1():
	#print top of grid
	print(space_plus+4*space_dash+space_plus+4*space_dash+space_plus)
	
	#print row 1 boxes
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)
	
	#print mid-grid border
	print(space_plus+4*space_dash+space_plus+4*space_dash+space_plus)
	
	#print row 2 boxes
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)
	print(space_pipe+4*space_space+space_pipe+4*space_space+space_pipe)

	#print bottom of grid
	print(space_plus+4*space_dash+space_plus+4*space_dash+space_plus)

#Part2 n-sized 2x2 grid
import math
def print_grid2(n):
	n2=math.floor(n/2)
	#print top of grid
	print(space_plus+n2*space_dash+space_plus+n2*space_dash+space_plus)
	
	#print row 1 boxes
	for r1 in range(n2): 
		print(space_pipe+n2*space_space+space_pipe+n2*space_space+space_pipe)
	
	#print mid grid border
	print(space_plus+n2*space_dash+space_plus+n2*space_dash+space_plus)

	#print row 2 boxes
	for r2 in range(n2): 
		print(space_pipe+n2*space_space+space_pipe+n2*space_space+space_pipe)

	#print bottom of grid
	print(space_plus+n2*space_dash+space_plus+n2*space_dash+space_plus)


#Part3 n-sized ZxZ grid
def print_grid3(z,n):
	#height/width of grid is n*z+z+1
	hw=n*z+z+1
	for i in range(hw):
		if i%(n+1)==0:
			print((space_plus+n*space_dash)*z+space_plus)
		else:
			print((space_pipe+n*space_space)*z+space_pipe)

