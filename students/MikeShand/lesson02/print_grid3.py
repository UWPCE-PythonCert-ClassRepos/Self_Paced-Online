def plus(n):
    print('+',n*'-', end=' ')

def minus(n):
    print('|',n*' ', end=' ')

def horizontal(n,m):
    for i in range(m):
        plus(n)
    print('+')

def vertical(n,m):
   for i in range(m):
        minus(n)
   print('|')

 # This is the fuction for the third grid exercise
 
def super_grid(n,m):
    for i in range(m):
        horizontal(n,m)
        for j in range(n):
            vertical(n,m)
    horizontal(n,m)

super_grid(3,4)
print("Hello")
