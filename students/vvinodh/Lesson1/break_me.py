def name_error_func():
    c=a+b
    name_error_func()


def type_error_func():
    a= 'vinodh'
    a=a + ' learning python'
    a=a +1
    print(a)
    type_error_func()

def attribute_error():
    import math
    print("Generating syntax error")
    x='Hello'
    math.calculate(x)

def syntax_error():
    x = 0
    if x ==0
    print(x)