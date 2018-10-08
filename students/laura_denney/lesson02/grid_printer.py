#-------------------------------------------------#
# Title: Grid Printer
# Dev:   LDenney
# Date:  October 3, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/3/18, Created File
#-------------------------------------------------#


plus = "+"
minus = " -"
line = "|"
space = " "
#print(
'''
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''
#)

def plus_row(size):
    print(plus + size * minus + " " + plus, end = "")
    print( size * minus + " " + plus)

def line_row(size):
    print(line + space * (size *2 + 1) + line, end = "")
    print(space * (size *2 + 1) + line)

def one_arg_grid(num):
    size = num // 2
    plus_row(size)
    for x in range(size):
        line_row(size)
    plus_row(size)
    for x in range(size):
        line_row(size)
    plus_row(size)

def plus_row1(rc, size):
    for x in range(rc):
        print(plus + size * minus + " " , end = "")
    print(plus)

def line_row1(rc, size):
    for x in range(rc):
        print(line + space * (size *2 + 1), end = "")
    print(line)

def two_arg_grid(rc, size):
    for x in range(rc):
        plus_row1(rc,size)
        for x in range(size):
            line_row1(rc, size)
    plus_row1(rc, size)

def askargs():
    args = ""
    while args != "exit":
        print()
        args = input("How many arguments (1 or 2) would you like for your grid? (type exit to exit): ")
        if args == "1":
            num = input("Please choose the size of your grid: ")
            one_arg_grid(int(num))
        elif args == "2":
            rc = input("Please choose the number of rows/columns: ")
            size = input("Please choose the number of units: ")
            two_arg_grid(int(rc), int(size))
        elif args == 'exit':
            break
        else:
            args = input("Please choose a valid number (1 or 2) of arguments or type exit to exit: ")


if __name__ == "__main__":
    askargs()
