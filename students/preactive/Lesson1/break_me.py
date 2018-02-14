def nameErrFunc():
    print("NameError")
    print(undefinedVar)

def typeErrFunc():
    print("TypeError")
    print(1+"1")

def attribErrFunc():
    print("AttributeError")
    a = 123
    a.sort()

def syntaxErrFunc():
    print("SyntaxError")
    print("Muh Bad";//)


#nameErrFunc()
#typeErrFunc()
#attribErrFunc()
syntaxErrFunc()