# print simple grid - part 2. Accept one parameter

# function - print grid accepting one parameter
def func_print_grid(x):
	y = x // 2
	# print top line
	print('+', ' - '*y, '+', ' - '*y, '+')
	# print pre mid lines
	count = 0
	while count < y:
		print('|', ' - '*y, '|', ' - '*y, '+')
		count += 1
	# print mid line
	print('+', ' - '*y, '+', ' - '*y, '+')
	# print pre end lines
	count = 0
	while count < y:
		print('|', ' - '*y, '|', ' - '*y, '+')
		count += 1
	# print end line
	print('+', ' - '*y, '+', ' - '*y, '+')
	
func_print_grid(8)


