
## Ian Letourneau
## 04/24/2018
## A script to test various errors

def nameError():
	print (a)

def typeError():
	divide = "string"/2

def syntaxError():
	False = True

def attributeError():
	a = 5
	name = a.name()

nameError()
typeError()
syntaxError()
attributeError()
