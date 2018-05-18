def fibonacci(arg1):
	"""
	Return nth fibonacci number
	:param arg1: the n th number
	the first and second value of fibonacci is 0 and 1
	"""
	if arg1 == 0:
		return 0
	elif arg1 ==1:
		return 1
	elif type(arg1) == int and arg1 >1:
		return fibonacci(arg1-1) + fibonacci(arg1-2)
	else: print('Please enter valid integer number')
		
def lucas(arg1):
	"""
	Return nth lucas number
	:param arg1: the n th number
	the first and second value of lucas is 2 and 1
	"""
	if arg1 == 0:
		return 2
	elif arg1 ==1:
		return 1
	elif type(arg1) == int and arg1 >1:
		return lucas(arg1-1) + lucas(arg1-2)
	else: print('Please enter valid integer number')
		
		
def sum_series(arg1,arg2 = 0,arg3 = 1):
	"""
	Return nth number in the series
	:param arg1: the n th number in the series
	:param arg2: the first value in the series, the default is fibonacci number 0
	:param arg3: the second value in the series, the default is fibonacci number 1
	"""
	if arg1 == 0:
		return arg2
	elif arg1 ==1:
		return arg3
	elif type(arg1) == int and arg1 >1:
		return sum_series(arg1-1,arg2,arg3) + sum_series(arg1-2,arg2,arg3)
	else: print('Please enter valid integer number')
		
if __name__ == '__main__' :
	print('fibonacci number:')
	for i in range(10):
		print(fibonacci(i))
		
	print('lucas number:')	
	for i in range(10):
		print(lucas(i))
		
	print('fibonacci number:')	
	for i in range(10):		
		print(sum_series(i))
		
	print('lucas number:')	
	for i in range(10):		
		print(sum_series(i,2,1))
		
	print('series number starting with 4 and 6:')	
	for i in range(10):
		print(sum_series(i,4,6))
				
