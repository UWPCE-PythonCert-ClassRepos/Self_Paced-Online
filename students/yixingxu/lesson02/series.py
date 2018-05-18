def fibonacci(arg1):
	"""
	Return nth fibonacci number
	:param arg1: the n th number
	"""
	if arg1 == 0:
		return 0
	elif arg1 ==1:
		return 1
	elif type(arg1) == int and arg1 >1:
		return fibonacci(arg1-1) + fibonacci(arg1-2)
	else: print('Please enter valid integer number')
		
if __name__ == '__main__' :
	for i in range(10):
		print(fibonacci(i))