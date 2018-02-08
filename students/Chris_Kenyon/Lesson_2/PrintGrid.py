###Lesson 2 making a program for creating grids of various sizes###

#set values for simplicity
p = "+"
m = "-"
s = " "
v = "|"

###Part 1: Brute force###
#create a 2x2 grid of pre-specified size using print commands
print(p + (m*4) + p + (m*4) + p)
for i in range(4):
	print(v + (s *4) + v + (s*4) + v)
print(p + (m*4) + p + (m*4) + p)
for i in range(4):
	print(v + (s *4) + v + (s*4) + v)
print(p + (m*4) + p + (m*4) + p)

###Part 2: Making a basic function###
#create a 2x2 grid of defined size using a function

def print_grid(GridSize):
	"""Create a 2x2 grid with with grid size determined from function argument"""
	print(p + (m*GridSize) + p + (m*GridSize) + p)
	for i in range(GridSize):
		print(v + (s *GridSize) + v + (s*GridSize) + v)
	print(p + (m*GridSize) + p + (m*GridSize) + p)
	for i in range(GridSize):
		print(v + (s *GridSize) + v + (s*GridSize) + v)
	print(p + (m*GridSize) + p + (m*GridSize) + p)
	
###Part 3: Two Part Function###
#create a grid with variable rows and columns of variable size

def print_grid2(GridSize,RowCol):
	"""Create a grid with with grid size and number of rows and columns determined from function arguments"""
	if GridSize > 0 and RowCol > 0: #check for valid inputs
		#print the top line of the grid
		print(p, end = "")
		for i in range(RowCol):
			print((m*GridSize) + p, end = "")
		#print the rest of the grid
		for i in range(RowCol): #for each row specified by Row/Col
			for i in range(GridSize): #for each row specified to increase size based on Grid Size
				print()
				print(v, end = "")
				for i in range(RowCol):#for each column
					print((s*GridSize)+v, end = "")
			print()
			print(p, end = "")
			for i in range(RowCol):#for each column, add the cross lines and "-" spacers
				print((m*GridSize) + p, end = "")
	else:
		print("please specify valid integers greater than 0")












