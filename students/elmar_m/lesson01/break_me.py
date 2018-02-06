# Remove comment signs to test a function, 
# and keep the other functions commented out
# at that time. 

def create_attribute_error():
    '''
    This function creates an AttributeError
    '''
    a = 'string_one'
    d = a.non_existing_attribute()

create_attribute_error()

#def create_syntax_error():
#    '''
#    This function creates a SyntaxError
#    '''
#    mylist = ['string_one'; 'string_two';]
#    print(mylist)

#def create_type_error():
#    ''' 
#    This function creates a TypeError
#    '''
#    a = 'string_one'
#    b = 'string_two'
#    c = a * b
#
#create_type_error()

#def create_name_error():
#    ''' 
#    This function creates a NameError
#    '''
#    print(c)
#
#create_name_error()
