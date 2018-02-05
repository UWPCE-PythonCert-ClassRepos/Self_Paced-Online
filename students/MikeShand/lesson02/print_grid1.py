def plus(n):
    print('+',n*'-', end=' ')

def minus(n):
    print('|',n*' ', end=' ')

def horizontal(n):
    plus(n)
    plus(n)
    print('+')

def vertical(n):
    minus(n)
    minus(n)
    print('|')

#this is the function for the second grid exercise

def grid(n):
    horizontal(n)
    for i in range(n):
        vertical(n)
    horizontal(n)
    for i in range(n):
        vertical(n)
    horizontal(n)

grid(5)