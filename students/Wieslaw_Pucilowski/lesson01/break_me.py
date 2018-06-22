def func1():
	# NameError
	try:
		return(x+3)
	except NameError as e:
		print("Caught NameError exception:", e)

def func2():
	# TypeError
	try:
		a="string for test"
		b=12
		c=a+b
		return(c)
	except TypeError as e:
		print('Cought TypeError exception: ', e)

def func3():
	# SyntaxError
	try:
		code='1 +-/* 4'
		exec(code)
	except SyntaxError as e:
		print("Cought SyntaxError exception: ", e)
	
def func4():
	try:
		# AttributeError
		x=100
		x.split()
	except AttributeError as e:
		print("Cought AttributeError exception: ", e)