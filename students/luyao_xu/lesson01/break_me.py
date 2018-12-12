# Create a new directory in your working dir for the class:

# $ mkdir lesson01
# $ cd lesson01
# Add a new file to it called break_me.py

# In the break_me.py file write four simple Python functions:

# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError
# (hint – the interpreter will quit when it hits a Exception – so you can comment out all but the one you are testing at the moment)


def name_error():

    print(student)

def type_error():
    x = 5
    print x+student

def syntax_error():
    x =5
    y =6
    print x+y*5)

def attribute_error():
    x=5
    y=6
    return x+y+z
attribute_error()
