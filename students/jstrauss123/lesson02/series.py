# series function - compute fibonacci and lucas series

def fibonacci(n):
	count = 3
	fibvaln1 = 1
	fibvaln2 = 0
	nextval = fibvaln1 + fibvaln2
	# loop through series stopping at input + 1
	while count < n + 1:
		if count == n:
			print("The ", n," fibonacci series value is: ", nextval)
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
			print("The ", n," lucas series value is: ", nextval)
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
			print("The ", n," series value is: ", nextval)
		# add valn1 and valn2 for next number in series 
		valn2 = valn1
		valn1 = nextval
		nextval = valn1 + valn2
		count += 1
	# add assert tests.. ?

fibonacci(5)
lucas(5)
sum_series(5)
sum_series(5, 5, 10)


