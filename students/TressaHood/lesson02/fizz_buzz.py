#lesson 2, assignment fizz buzz

#define the main function
def main():

	#print 1 - 100 inclusive
	for i in range(1,101):
		
		#if it is a multiple of 3 and 5 print FizzBuzz
		if((i % 3 == 0) and (i % 5 == 0)):
			print("FizzBuzz")

		#if multiple of 3 print fizz
		elif( i % 3 == 0):
			print("Fizz")

		#if multiple of 5 print buzz
		elif( i % 5 == 0):
			print("Buzz")

		else:
			print(i)


#call the main function
main()
