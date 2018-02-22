

#part 2
def print_grid(n):
	#first (+-)row
	print('+', end=' ')
	for i in range(n//2):
		print('-', end=' ')
	print('+', end=' ')
	for i in range(n//2):
		print('-', end=' ')
	print('+')
	#second (|) row
	for i in range(n//2):
		print('|', end=' ')
		for i in range(n//2):
			print(' ', end=' ')
		print('|', end=' ')
		for i in range(n//2):
			print(' ', end=' ')
		print('|')
	#third (+-) rows
	print('+', end=' ')
	for i in range(n//2):
		print('-', end=' ')
	print('+', end=' ')
	for i in range(n//2):
		print('-', end=' ')
	print('+')
	#fourth (|) row
	for i in range(n//2):
		print('|', end=' ')
		for i in range(n//2):
			print(' ', end=' ')
		print('|', end=' ')
		for i in range(n//2):
			print(' ', end=' ')
		print('|')
	#last (+-) row
	print('+', end=' ')
	for i in range(n//2):
		print('-', end=' ')
	print('+', end=' ')
	for i in range(n//2):
		print('-', end=' ')
	print('+')

#part 3
def print_grid2(rows, size):
	for i in range(rows):
		for i in range(rows):
			print('+', end=' ')
			for i in range(size):
				print('-', end=' ')
		print('+')
		for i in range(size):
			for i in range(rows):
				print('|', end=' ')
				for i in range(size):
					print(' ', end=' ')
			print('|')
	for i in range(rows):
		print('+', end=' ')
		for i in range(size):
			print('-', end=' ')
	print('+')


#part 1
print('+ - - - - + - - - - +')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('+ - - - - + - - - - +')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('+ - - - - + - - - - +')
print_grid(3)
print_grid2(5, 3)
	

	
