#part 2, create the sections with a function
#define the print grid function
def print_grid_part2(x):
	size = x//2
	first = ("+ " + "- "*size)*2 + "+"
	second = ("\n" + ("| " + "  "*size)*2 + "|")*size
	print(first, second, "\n" + first, second, "\n" + first)

def print_grid_part3(x,y):
	dim = x
	size = y
	first = ("+ " + "- "*size)*dim + "+"
	second = ("\n" + ("| " + "  "*size)*dim + "|")*size
	for rnum in range(dim):
		print(first, second)

		#unless it is the bottom row
		if(rnum == dim-1):
			print(first)


#define the main function
def main():

	#part 1
	#create my sections manually
	first = ("+ " + "- "*4)*2 + "+"
	second = ("\n" + ("|" + "\t " + " " + "\t " + " ")*2 + "  |")*4
	print("This is part one:")
	print(first, second, "\n" + first, second, "\n" + first)
	print()

	#now do part 2
	print("This is part two:")
	print_grid_part2(3)
	print_grid_part2(8)
	print_grid_part2(15)
	print()

	#now do part 3
	print("This is part three:")
	print_grid_part3(3,4)
	print_grid_part3(5,3)



#call the main function
main()
