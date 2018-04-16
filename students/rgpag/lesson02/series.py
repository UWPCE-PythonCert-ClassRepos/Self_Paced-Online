def fibonacci(n):
	"""fibonacci(n) - return "n"th value of the fibonacci series"""
	#fibL1=1
	#fibL2=0
	#if n<0:
	#	print("please enter positive int value")

	#elif n==0:
	#	return 0

	#elif n==1:
	#	return 1

	#else:
	#	for i in range(n-1):
	#		fibC=fibL1+fibL2
	#		fibL2=fibL1
	#		fibL1=fibC
	#	return fibC
	return sum_series(n)

def lucas(n):
	"""lucas(n) - return "n"th value of the lucas series"""
	#lucL1=1
	#lucL2=2
	#if n<0:
	#	print("please enter positive int value")

	#elif n==0:
	#	return 2

	#elif n==1:
	#	return 1

	#else:
	#	for i in range(n-1):
	#		lucC=lucL1+lucL2
	#		lucL2=lucL1
	#		lucL1=lucC
	#	return lucC
	return sum_series(n,2,1)
	
def sum_series(n,v1=0,v2=1):
	"""sum series(n,v1=0,v2=1) - return "n"th value of sum series having v1 and v2 as first and second values"""
	L1=v2
	L2=v1
	if n<0:
		print("please enter positive int value")

	elif n==0:
		return v1

	elif n==1:
		return v2

	else:
		for i in range(n-1):
			C=L1+L2
			L2=L1
			L1=C
		return C	