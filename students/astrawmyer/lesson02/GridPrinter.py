# Function for Part 1 of assignment 2
# Prints a fixed size 2x2 grid
def Part1():
    row = '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+'
    col = '|' + ' ' * 9 + '|' + ' ' * 9 + '|'
    print(row)
    print(col)
    print(col)
    print(col)
    print(col)
    print(row)
    print(col)
    print(col)
    print(col)
    print(col)
    print(row)


#Part1()

# Function for Part 2 of assignment
# Prints a 2x2 grid with customized sizes based on input to function
def print_grid(n):
    row = ("+ " + '- '*n)*2 + '+'
    col = ('|' + ' ' * (2*n+1))*2 + '|'
    for i in range(2):
        print(row)
        for j in range(n):
            print(col)
    print(row)



#print_grid(15)

# Function for part 3 of assignment
# Prints grid with specificized number of rows and columns and size of cells.
# m is grid size
# n is cell size
def print_grid2(m,n):
    row = ("+ " + '- '*n)*m + '+'
    col = ('|' + ' ' * (2*n+1))*m + '|'
    for i in range(m):
        print(row)
        for j in range(n):
            print(col)
    print(row)

    
#print_grid2(5,3)