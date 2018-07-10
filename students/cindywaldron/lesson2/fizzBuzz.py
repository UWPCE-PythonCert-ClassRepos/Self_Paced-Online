def fizzBuzz():
	i = 1
	fizz = 'Fizz'
	buzz = 'Buzz'
	result = ''
	while i <= 100:
		if ( i % 3 == 0 and i % 5 == 0):
			result = fizz+buzz
		elif ( i %3 == 0 ):
			result = fizz
		elif ( i % 5 == 0 ):
			result = buzz
		else:
			result = i
		print(result)
		i = i + 1

fizzBuzz()