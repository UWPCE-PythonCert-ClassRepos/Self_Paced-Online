def fun1():
    #name error
    print(x)
    return None
    

def fun2():
    #type error
    len(42)
    return None

def fun3():
    #syntax error
    print "hello"
    return None
    
def fun4():
    #attribute error
    x = 5
    x.append(2)
    return None