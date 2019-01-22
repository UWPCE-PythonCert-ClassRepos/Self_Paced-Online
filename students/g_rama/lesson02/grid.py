
#Part1 Printing with simple print statements

print('+' + 4* '-' + '+' + 4*'-' + '+')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('+' + 4* '-' + '+' + 4*'-' + '+')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('|' + 4* ' ' + '|' + 4*' ' + '|')
print('+' + 4* '-' + '+' + 4*'-' + '+')


#Part2 Printing grid with functions

def print_pipe(pipe_size):
    for i in range(pipe_size):
        print('|' + pipe_size * ' ' + '|' + pipe_size * ' ' + '|')
def print_rowpatteren(row_size):
    print('+' + row_size * '-' + '+' + row_size * '-' + '+')

def print_grid(n):
    if n%2 == 0:
        s=n//2
        print_rowpatteren(s)
        print_pipe(s)
        print_rowpatteren(s)
        print_pipe(s)
        print_rowpatteren(s)
    else:
        s=(n-1)//2
        print_rowpatteren(s)
        print_pipe(s)
        print_rowpatteren(s)
        print_pipe(s)
        print_rowpatteren(s)

print_grid(30)
print_grid(29)

#Part3 Printing grid with function and two parameters

def print_rowedge(num_cubes,size_cube):
    print('+', end='')
    for cube in range(num_cubes):
        print(size_cube * '-', end='+')
    print()
def print_rowmiddle(num_cubes,size_cube):
    print('|', end='')
    for cube in range(num_cubes):
        print(size_cube * ' ', end='|')
    print()


def print_grid(num_cubes,size_cube):
    for row in range(num_cubes):
        print_rowedge(num_cubes, size_cube)
        for size in range(size_cube):
            print_rowmiddle(num_cubes, size_cube)
    print_rowedge(num_cubes, size_cube)



print_grid(3,3)
print_grid(9,5)
print_grid(4,8)
