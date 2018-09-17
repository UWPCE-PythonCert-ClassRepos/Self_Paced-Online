def fibonacci(n):
	assert (n > 0), "Must be greater than 0"
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

#TEST FUCNTIONS
print("Testing each function")
print("Testing fionacci(6)")
fibonacci(6)
print()
print("Testing lucas(8)")
lucas(8)
print()
print("Testing sum_series(6)")
sum_series(6)
print()
print("Testing sum_series(6,5,6)")
sum_series(6, 5, 6)