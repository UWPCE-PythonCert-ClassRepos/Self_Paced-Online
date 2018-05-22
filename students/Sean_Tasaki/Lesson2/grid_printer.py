
def grid_printer_part1():
	print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('|' + ' ' * 9 + '|' + ' ' * 9 + '|')
	print()
	print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')
print('Printing grid_printer_part1()')
grid_printer_part1()
print()

def grid_printer_part2(n = 3):
	new = n//2
	x = ' -'
	line = '|'
	plus = '+'
    
	if n % 2 == 0:
		string1 = line + ' ' * n + ' ' + line + ' ' * n + ' ' + line + '\n'
	else:
		string1 = line + ' ' * n + line + ' ' * n + line + '\n'
    
	string2 = plus + x * new + ' ' + plus + x * new + ' ' + plus + '\n'
	print(string2 + string1 * new + string2 + string1 * new + string2)
print('Printing grid_printer_part2(n = 3)')    
grid_printer_part2()
print()

def grid_printer_part3(rc = 5, s = 3):
	x = ' -' * s
	line = '|'
	space = ' ' * (s * 2 + 1)
	plus = '+'
    
	string1 = (line + space) * rc + line + "\n"
   
	string2 = (plus + x + " ") * rc + plus + "\n"
    
	print((string2 + (string1 * s)) * rc + string2)
    
print("Printing grid_printer_part3()")      
grid_printer_part3()

     