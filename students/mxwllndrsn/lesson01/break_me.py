# lesson01
# ma 072718
# four simple & broken functions

print("Break_me.py loaded")
print("callable functions: name_error(), type_error(x), attribute_error(x)")

def name_error():
    return a

def type_error(x):
    x += 'asdf'
    return x

# def syntax_error():
#     \][\=-]

#syntax_error() throws exception upon loading in iPython

def attribute_error(x):
    return x.attribute

