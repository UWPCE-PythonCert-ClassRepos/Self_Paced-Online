def NameErrorFunc():
    x = 1
    print(y)

def TypeErrorFunc():
    x = 1
    y = '2'
    return x + y

def SyntaxErrorFunc():
    print(x==;)

def AttributeErrorFunc():
    x = 1
    x.getSomeValue()
