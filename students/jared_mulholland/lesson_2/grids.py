"""
Prob 1: Grids

Goal - Write a function that draws a grid (see homework page)
"""
def grid():
    print("+","-" * 4,"+","-" * 4,"+")
    for i in range(4):
        print("|"," " * 4,"|"," " * 4,"|")

    print("+","-" * 4,"+","-" * 4,"+")
    for i in range(4):
        print("|"," " * 4,"|"," " * 4,"|")

    print("+","-" * 4,"+","-" * 4,"+")

"""
more general:
Write a function print_grid(n) that takes one integer argument and prints a 
grid just like before, BUT the size of the grid is given by the argument.
"""

def print_grid(x):
    import math 
    print("+", "-" * math.floor(x/2), "+", "-" * math.floor(x/2), "+")
    
    for i in range(math.floor(x/2)):
        print("|"," " * math.floor(x/2), "|", " " * math.floor(x/2), "|")
    
    print("+", "-" * math.floor(x/2), "+", "-" * math.floor(x/2), "+")
    
    for i in range(math.floor(x/2)):
        print("|"," " * math.floor(x/2), "|", " " * math.floor(x/2), "|")
    
    print("+", "-" * math.floor(x/2), "+", "-" * math.floor(x/2), "+")

"""
even more general:
Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.
"""

def print_grid2(x,y):
    """rows and columns will by x, number of dashes and pipes will be y"""
    import math
    pl = "+"
    d = "-" * y
    s = " " * y
    pi = "|" 
    
    for i in range(x):
        print((pl+d)*x+pl)
        for j in range(y):
            print((pi+s)*x+pi)
    print((pl+d)*x+pl)