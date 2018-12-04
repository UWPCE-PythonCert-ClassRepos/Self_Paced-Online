#!/usr/bin/env Python3


top = '+----+'
addTop = '----+'
edges = '|    |'
addEdge = '    |'

def gridFun(m):
	for _ in range(m):
		print(top + addTop * (m-1))
		for _ in range(4):
			print(edges + addEdge * (m-1))
	for _ in range(1):
		print(top + addTop * (m-1)) 

	

print("Welcome to Grid Fun - where all you can do is create square grids of any size!")
print()
print("To create a grid, all you have to do is type 'gridFun(m)', where m is the number of rows and colums.")
print()
print("Example:  gridFun(3) will create a 3 x 3 grid containing three rows and three columns.")

	



