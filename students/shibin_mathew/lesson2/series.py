def fibonacci(n):
	first = 0
	second = 0
	third = 0
	listT= []
	for i in range(0,100):
		'''This function returns the nth value of the fibonacci seires'''
		if i==0:
			listT.append(i)
			first = i

		elif i==1:
			listT.append(i)
			second = i
		else:
			listT.append(first+second)
			third = first
			first = second
			second = third+second


			# print(i,i-1, i-2)

	return listT[n]

if __name__== '__main__':
	for i in range(0,10):
		print(fibonacci(i))

