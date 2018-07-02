#Description: Program that prints grids 
#Author: Andy Kwok
#Last Updated: 07/01/2018
#ChangeLog: 
#			v1.0 - Initialization


#Function that prints a 2x2 grid
def print_grid_basic():
	for j in range(2):	
		print('+' + ' - '*4 + '+' +  ' - '*4 + '+')
		for i in range(4):	
			print('|' + '   '*4 + '|' +  '   '*4 + '|')	
	print('+' + ' - '*4 + '+' +  ' - '*4 + '+')
	
#Function that prints a 2x2 grid with various size per input value (grid size increase by value)
def print_grid_one(x):
	y = int(x/2)
	for j in range(2):	
		print('+' + ' - '*y + '+' +  ' - '*y + '+')
		for i in range(y):	
			print('|' + '   '*y + '|' +  '   '*y + '|')	
	print('+' + ' - '*y + '+' +  ' - '*y + '+')

	
#Function that prints a nxn grid with various size per input values
#First parameter is number of squares in each row/column, n
#Second parameter is the width of each square 
def print_grid_multi(x,y):
	for j in range(x):	
		for k in range(x):
			print('+' + ' - '*y , end=' ')
		print('+')
		for i in range(x):	
				print('|' + '   '*y , end=' ')
		print('|')
	for k in range(x):
		print('+' + ' - '*y , end=' ')
	print('+')