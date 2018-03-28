def get_name_error():
	print (a)
	
def get_type_error():
	a = 5
	b = '5'
	return(a + b)
	
def get_syntax_error():
	a = 5
	b =. a
	
def get_attribute_error():
	a = 5
	a.split
	
get_name_error()
get_type_error()
get_syntax_error()
get_attribute_error()