x = 32
y = 33
z = 34

def fun(y,z):
    print(x,y,z)
    
def bad_fun():
    y = x
    print(x)
    print(y)
    
fun(3,4)
bad_fun()