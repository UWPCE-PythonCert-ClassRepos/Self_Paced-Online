def test():
	
	for i in range(100):
		if i == 0:
			print()
		elif(i%3 == 0 and i%5!=0):
			print("Fizz")
		elif(i%5== 0 and i%3!=0):
			print("Buzz")
		elif(i%3==0 and i%5==0):
			print("FizzBuzz")
		else:
			print(i)

		i = i + 1