# Function for Part 1 of assignment 2
# Prints a fixed size 2x2 grid
def Part1():
    Row = '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+'
    Col = '|' + ' ' * 9 + '|' + ' ' * 9 + '|'
    print(Row)
    print(Col)
    print(Col)
    print(Col)
    print(Col)
    print(Row)
    print(Col)
    print(Col)
    print(Col)
    print(Col)
    print(Row)
    return

#Part1()

# Function for Part 2 of assignment
# Prints a 2x2 grid with customized sizes based on input to function
def print_grid(n):
    Row = ("+ " + '- '*n)*2 + '+'
    Col = ('|' + ' ' * (2*n+1))*2 + '|'
    for i in range(2):
        print(Row)
        for j in range(n):
            print(Col)
    print(Row)
    return


print_grid(15)

# Function for part 3 of assignment
# Prints grid with specificized number of rows and columns and size of cells.
# m is grid size
# n is cell size
def print_grid2(m,n):
    Row = ("+ " + '- '*n)*m + '+'
    Col = ('|' + ' ' * (2*n+1))*m + '|'
    for i in range(m):
        print(Row)
        for j in range(n):
            print(Col)
    print(Row)
    return
    
print_grid2(5,3)