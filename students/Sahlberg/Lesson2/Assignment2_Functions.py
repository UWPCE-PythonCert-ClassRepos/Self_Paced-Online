"""Ian Sahlberg
Assignment 2 - Grid functions
Self paced
December 10, 2018"""

def func1():
    """This function prints out a simple box."""
    print("+ - - - - + - - - - +\n|         |         |\n|         |         |\n|         |         |\n|         |         |")
    print("+ - - - - + - - - - +\n|         |         |\n|         |         |\n|         |         |\n|         |         |")
    print("+ - - - - + - - - - +")

def print_grid(n):
    """This function prints out a box of size(n)."""
    dash = n//2*'- '
    num = n//2
    y = '|'
    x = num*'  '
    layer1 = '+'+dash+'+'+dash+'+'
    mid = y + x + y + x + y

    print(layer1)
    print(num*(mid+'\n'),end = "")
    print(layer1)
    print(num * (mid + '\n'), end="")
    print(layer1)

def funct3(size,width):
    """This function prints out a box defined by number of columns (size)
    and width of columns (width)."""
    dash = width*'- '
    spaces = (2*width)*' '
    columns = width
    print(size * ('+' + dash)+'+')

    for i in range(size):
        count = columns
        while count > 0:
            print((size)*('|'+ spaces)+'|')
            count -=1

        print(size * ('+' + dash) + '+')


#Function calls

func1()

print_grid(4)

funct3(5,13)
