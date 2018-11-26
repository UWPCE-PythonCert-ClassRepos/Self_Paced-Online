# series function - compute fibonacci and lucas series

def fibonacci(n):
	count = 3
	fibvaln1 = 1
	fibvaln2 = 0
	nextval = fibvaln1 + fibvaln2
	# loop through series stopping at input + 1
	while count < n + 1:
		if count == n:
			return nextval
		#print("fibvaln1 = ", fibvaln1, "fibvaln2 = ", fibvaln2, "nextval = ", nextval)
		# add fibvaln1 and fibvaln2 for next number in series 
		fibvaln2 = fibvaln1
		fibvaln1 = nextval
		nextval = fibvaln1 + fibvaln2
		count += 1
	
def lucas(n):
	count = 3
	lucvaln1 = 1
	lucvaln2 = 2
	nextval = lucvaln1 + lucvaln2
	# loop through series stopping at input + 1
	while count < n + 1:
		if count == n:
			return nextval
		# add lucvaln1 and lucvaln2 for next number in series 
		lucvaln2 = lucvaln1
		lucvaln1 = nextval
		nextval = lucvaln1 + lucvaln2
		count += 1

def sum_series(n, y=0, z=1):
	count = 3
	valn1 = z
	valn2 = y
	nextval = valn1 + valn2
	# loop through series stopping at input + 1
	while count < n + 1:
		if count == n:
			return nextval
		# add valn1 and valn2 for next number in series 
		valn2 = valn1
		valn1 = nextval
		nextval = valn1 + valn2
		count += 1


fibonacci(5)
lucas(5)
sum_series(5)
sum_series(5, 5, 10)

# assert tests
if __name__ == "__main__":
	# this runs only if run as a script
	print("Running the tests")
	# validate fibonacci function returning appropriate value
	assert fibonacci(5) == 3
	# validate lucas function returning appropriate value
	assert lucas(5) == 7
	# validate sum_series function returning appropriate value for default
	assert sum_series(5) == 3
	
	print("the tests passed")
	
	

