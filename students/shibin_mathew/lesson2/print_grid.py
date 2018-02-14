
def print_grids(size,n):

	plus = '+ '
	minus = '- '
	sym = '| '
	r1c1 = (plus)
	r1c2 = (minus*(n))
	row1 = r1c1+r1c2
	row2 = sym+'  '*(n)
	

	def print_n_times(n): #function to print the units
		for i in range(0,n):
			print(row2*(size+1))
		
	print(row1*(size)+r1c1) #print the first row

	for x in range(0,size): 
		print_n_times(n)
		print(row1*(size)+r1c1)

if __name__ == '__main__':
	#main function to test print_grids function
	print_grids(4,8)
	print_grids(5,3)


