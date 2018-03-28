def getNameError():
	print (a)
	
def getTypeError():
	a = 5
	b = '5'
	return(a + b)
	
def getSyntaxError():
	a = 5
	b =. a
	
def getAttributeError():
	a = 5
	a.split
	
getNameError()
getTypeError()
getSyntaxError()
getAttributeError()