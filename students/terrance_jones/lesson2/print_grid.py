#Part 1
def print_grid():
	gridrow =2
	gd = 4 # number of spaces between plus signs
	plus = '+'
	minus = '-'
	vbar = "|"
	space = " "

	line = plus + (minus * gd) + plus + (minus* gd) + plus
	line2 = vbar + (space * gd) + vbar + (space * gd) + vbar


	for i in range(gridrow):
		print(line)
		for i in range(gd):
			print(line2) 
	print(line)


# Part 2
def print_grid(x):
	
	
		#print line 1
	print('+', end=' ')	
	columns = 0
	while (columns < (x//2)):
		print('-', end=' ')
		columns = columns + 1
		if(columns>=(x//2)):
			print('+', end=' ')
	columns = 0		
	while (columns < (x//2)):
		print('-', end=' ')
		columns = columns + 1
		if(columns >= (x//2)):
			print('+')


			#print line 2

	counter = 0
	while (counter <= (x//2)):
		
		print('|', end=' ')	
		columns = 0
		while (columns < (x//2)):
			print(" ", end=' ')
			columns = columns + 1
			if(columns >= (x//2)):
				print('|', end=' ')
		columns = 0		
		while (columns < (x//2)):
			print(" ", end=' ')
			columns = columns + 1
			if(columns >= (x//2)):
				print('|')
		counter = counter + 1


#print line 1
	print('+', end=' ')	
	columns = 0
	while (columns < (x//2)):
		print('-', end=' ')
		columns = columns + 1
		if(columns>=(x//2)):
			print('+', end=' ')
	columns = 0		
	while (columns < (x//2)):
		print('-', end=' ')
		columns = columns + 1
		if(columns >= (x//2)):
			print('+')


			#print line 2

	counter = 0
	while (counter <= (x//2)):
		
		print('|', end=' ')	
		columns = 0
		while (columns < (x//2)):
			print(" ", end=' ')
			columns = columns + 1
			if(columns >= (x//2)):
				print('|', end=' ')
		columns = 0		
		while (columns < (x//2)):
			print(" ", end=' ')
			columns = columns + 1
			if(columns >= (x//2)):
				print('|')
		counter = counter + 1


	#print line 1
	print('+', end=' ')	
	columns = 0
	while (columns < (x//2)):
		print('-', end=' ')
		columns = columns + 1
		if(columns>=(x//2)):
			print('+', end=' ')
	columns = 0		
	while (columns < (x//2)):
		print('-', end=' ')
		columns = columns + 1
		if(columns >= (x//2)):
			print('+')


# Part 3
def print_grid(n, x):	
	rowcount = 0
	for rowcount in range(n):
		line=''
		minus = ''
		columns = 0
		counter = 0
		# PRINT LINE 1
		while(counter < n):
				#print line 1
			line = '+'
			columns = 0
			while (columns < (x//2)):
				line = line + '-'
				columns = columns + 1
				if(columns>=(x//2)):
					print(line, end = '')
			counter = counter + 1
				
			if counter == n:
				print("+")
				line=''
		counter = 0

		# PRINT LINE 2
		rowcount = 0
		for rowcount in range(n):
			while(counter < n):
					#print line 2
				line = '|'
				columns = 0
				while (columns < (x//2)):
					line = line + " "
					columns = columns + 1
					if(columns>=(x//2)):
						print(line, end = '')
				counter = counter + 1
				
				if counter == n:
					print("|")
					line=''
			
			counter = 0

		
	rowcount=rowcount + 1
	if( rowcount == n):
		# PRINT LINE 1
		while(counter < n):
				#print line 1
			line = '+'
			columns = 0
			while (columns < (x//2)):
				line = line + '-'
				columns = columns + 1
				if(columns>=(x//2)):
					print(line, end = '')
			counter = counter + 1
				
			if counter == n:
				print("+")
				line=''
		counter = 0