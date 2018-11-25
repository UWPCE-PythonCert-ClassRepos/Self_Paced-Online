# print simple grid - part 3. Accept two parameters

# function - print grid accepting one parameter
def func_print_grid(z, x):
	y = x // 2
	# print top line, one grid at a time, loop through variable z
	count = 0
	while count < z:
		print('+', ' - '*y, end = ' ')
		count += 1
	print('+')
	# print pre mid lines, loop through variable y and z
	count = 0
	count1 = 0
	while count < x:
		print("loop through rows")
		while count1 < x:
			print('|', ' - '*y, end = ' ')
			count1 += 1
			print('|')
		count += 1
		count1 = 0
		
	#print('| - end')
	# print mid line, one grid at a time, loop through variable z
	count = 0
	while count < z:
		print('+', ' - '*y, end = ' ')
		count += 1
	print('+')
	# print pre end lines
	count = 0
	while count < y:
		print('|', ' - '*y, '|', ' - '*y, '+')
		count += 1
	# print bottom line, one grid at a time, loop through variable z
	count = 0
	while count < z:
		print('+', ' - '*y, end = ' ')
		count += 1
	print('+')
	
func_print_grid(3,4)


