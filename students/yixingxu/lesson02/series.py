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
		
if __name__ == '__main__' :
	for i in range(10):
		print(fibonacci(i))
	for i in range(10):
		print(lucas(i))