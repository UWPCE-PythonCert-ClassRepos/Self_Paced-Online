# -------------------------------------#
# Desc: Functions which throw four most common exceptions: NameError, TypeError, SyntaxError, AttributeError
# Dev: Will White
# Date: 4/1/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#

def name_error():
    print(x)  # Prints an undefined variable

def type_error():
    X = 7 + "x"  # Combines and integer with a string

def syntax_error():
    for i im range(1, 10):  # Error in the syntax: "im" instead of "in"
        print(i)

def attribute_error():
    x = "Hi"
    x.append("Hello")  # String variable types do not have an append attribute
