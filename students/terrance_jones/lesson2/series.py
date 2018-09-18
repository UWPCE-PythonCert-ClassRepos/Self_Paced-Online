def fibonacci(n):
	counter = 0
	a = 0
	b = 1

	print(a, end= '')
	print(b, end='')

	for counter in range(n):
		c = a + b
		print(c, end= '')
		a=b
		b=c
		counter = counter + 1
	
	if (counter == n):
		return True
	else:
		return False


def lucas(n):
	counter = 0
	a = 2
	b = 1

	print(a, end='')
	print(b, end='')

	for counter in range(n):
		c = a + b
		print(c, end='')
		a=b
		b=c
		counter = counter + 1

	if (counter == n):
		return True
	else:
		return False


def sum_series(n, a=0, b=1):
	if ( a != 0 and b != 1):
		counter = 0
		
		print(a, end='')
		print(b, end='')

		for counter in range(n):
			c = a + b
			print(c, end='')
			a=b
			b=c
			counter = counter + 1

		if (counter == n):
			return True
		else:
			return False
	else:
		counter = 0
		a = 0
		b = 1

		print(a, end='')
		print(b, end='')

		for counter in range(n):
			c = a + b
			print(c, end='')
			a=b
			b=c
			counter = counter + 1

		if (counter == n):
			return True
		else:
			return False



if __name__ == '__main__':
	print("testing")
	print()
	assert fibonacci(6) == True
	print()
	assert lucas(5) == True
	print()
	assert sum_series(3,4,5) == True
	print()
	print("testing passed")