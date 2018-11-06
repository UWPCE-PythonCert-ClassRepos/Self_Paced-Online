def name_error():
    print1()

def type_error():
    assert(5 + "5") == True

#def syntax_error():
#    "nt()")

def attribute_error():
    a = 8
    a.append(5)

#name_error()
type_error()
#syntax_error()
#attribute_error()