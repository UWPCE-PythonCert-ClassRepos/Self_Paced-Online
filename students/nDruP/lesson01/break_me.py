def nameError():
    18+name*7

def typeError():
    a = 5
    b = '6'
    c = a+b

def attrError():
    import math
    math.random()

'''
def synError():
    def javaSyn(){
        a = 'gaahhh'
    }
'''

#More Errors for funsies
def divByZeroError():
    x = 17/0

def importError():
    import badStuff

def indexError():
    x = [None]*13
    y = x[13]

def overflowError():
    x = 2048
    print("Press CTRL+C to stop")
    while x > 0:
        x = x*x*x*x*x*x*x*x


#overflowError()
#indexError()
#divByZeroError()
#importError()
#nameError()
#typeError()
#attrError()


