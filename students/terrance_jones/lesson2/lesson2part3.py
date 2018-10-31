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