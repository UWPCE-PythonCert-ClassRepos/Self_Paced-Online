def fibonacci(n):
	'''Returns the nth value in the fibonacci series'''
	fibonacci_list = [0,1]

	for number in range(1,n):
		fibonacci_list.append(fibonacci_list[number]+fibonacci_list[number-1])

	return fibonacci_list[n-1]


def lucas(n):
	'''Returns the nth value in the lucas series'''
	lucas_list = [2,1]
	
	for number in range(1,n):
		lucas_list.append(lucas_list[number]+lucas_list[number-1])

	return lucas_list[n-1]


def sum_series(n, first_number = 0, second_number = 1):
	'''Returns the nth value in a sum series, where you can dictate the first and second numbers of the series'''
	sum_list = [first_number, second_number]
	
	for number in range(1,n):
		sum_list.append(sum_list[number]+sum_list[number-1])

	return sum_list[n-1]



if __name__ == '__main__':
	'''Testing the three functions for accuracy'''

	#Testing the fibonacci function
	assert fibonacci(3) == 1
	assert fibonacci(7) == 8
	assert fibonacci(12) == 89

	#Testing the lucas fuction
	assert lucas(3) == 3
	assert lucas(7) == 18
	assert lucas(12) == 199

	#Testing the sum_series function
	assert sum_series(3) == 1
	assert sum_series(3) == fibonacci(3)
	assert sum_series(5,2,1) == lucas(5)
	assert sum_series(5,7,3) == 23










