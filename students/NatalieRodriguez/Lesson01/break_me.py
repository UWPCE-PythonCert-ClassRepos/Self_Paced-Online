def NameError():
     input_variable = input ("Enter your name: ")
print ("your name is" + input_variable)
"""The term input_variable is not defined, should throw a name error"""

"""Type Error"""
'dogs' + 3
"""this is an unsupported operand type - cannot add a string and an integer"""


"""Syntax Error"""
def SyntaxError() #writing the code without a colon throws a Syntax Error


"""Attribute Error"""
anInt = 8
anInt.append(4)

