def fibonacci(n):
	'''This function returns the nth value of the fibonacci seires'''
	first = 0
	second = 0
	third = 0
	listT= []
	for i in range(0,100):
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

	return listT[n-1]

def lucas(n):
	'''This function returns the nth value of the lucas seires'''
	first = 0
	second = 0
	third = 0
	listL = []
	for i in range(0,100):
		if i == 0:
			listL.append(2) #first number in the lucas sequence is 2
			first = 2
		elif i == 1:
			listL.append(1) #second number in the lucas sequence is 1
			second = 1
		else:
			listL.append(first+second)
			third = first
			first = second 
			second = third+second
	return listL[n-1]



def sum_series(n, firstPar = 0, secondPar = 1):
	#Generatlized function that implements the logic behind the fibonacci sequence and the lucas sequence
	first = 0 #initial value
	second = 0 #initial value
	third = 0 #initial value
	listS = []
	for i in range(0,100): #default parameter set to 100
		if i == 0:
			listS.append(firstPar)
			first = firstPar
		elif i == 1:
			listS.append(secondPar)
			second = secondPar
		else:
			listS.append(first+second)
			third = first
			first = second #previous value: sum_series(n-1)
			second = third+second #previous value: sum_series(n-2)
	return listS[n-1] 

if __name__== '__main__':
	#assert statements to test functionalities of the sum_series function
	assert sum_series(1) == 0 #This assert statement should return the first parameter of the fibonacci sequence
	assert sum_series(4,0,1) == 2 #This assert statement should return the fourth parameter of the fibonacci sequence
	assert sum_series(1,2,1) == 2 #This assert statement should return the first parameter of the lucas sequence
	assert sum_series(5,2,1) == 7  #This assert statement should return the fifth parameter of the lucas sequence


