# series function - compute fibonacci and lucas series

def fibonacci(n):
	count = 2
	fibvaln1 = 0
	fibvaln2 = 1
	nextval = fibvaln1 + fibvaln2
	while count < 50:
		if count == n:
			print("The ", n," fibonacci series value is: ", nextval)
		#print("fibvaln1 = ", fibvaln1, "fibvaln2 = ", fibvaln2, "nextval = ", nextval)
		# add fibvaln1 and fibvaln2 for next number in series 
		fibvaln2 = fibvaln1
		fibvaln1 = nextval
		nextval = fibvaln1 + fibvaln2
		count += 1
	
def lucas(n):
	count = 0
	l0 = 2
	l1 = 1
	lucvaln1 = l0 + l1
	lucvaln2 = l1
	nextval = lucvaln1 + lucvaln2
	while count < 50:
		if count == n:
			print("The ", n," lucas series value is: ", nextval)
		print("lucvaln1 = ", lucvaln1, "fibvaln2 = ", lucvaln2, "nextval = ", nextval)
		# add lucvaln1 and lucvaln2 for next number in series 
		lucvaln2 = lucvaln1
		lucvaln1 = nextval
		nextval = lucvaln1 + lucvaln2
		count += 1

#def sum_series(x, y, z):


fibonacci(6)
#lucas(5)

