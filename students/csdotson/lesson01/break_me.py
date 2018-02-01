# Task 1: Explore Errors

def name_error():
    pass
end  # NameError: name 'end' is not defined

def type_error():
    n = True
    len(n) # TypeError: object of type 'bool' has no len()

def syntax_error():
    i = 'Hello'
    print i  # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(int i)?

def attribute_error():
    str = 'attribute'
    return str.length  # AttributeError: 'str' object has no attribute 'length'
