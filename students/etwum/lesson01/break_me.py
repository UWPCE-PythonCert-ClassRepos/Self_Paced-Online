def name_error():
    #a name error is expected to occur
    x = 5
    y = 6
    print(w)


name_error()


def type_error():
    #a type error is expected to occur
    x = 5
    y = "4"
    z = x + y
    print(z)


type_error()

def syntax_error():
    #a syntax error is expected to occur
    print x

syntax_error()


def attribute_error():
    #an attribute error is expected to occur
    x = 5
    x.random


attribute_error()