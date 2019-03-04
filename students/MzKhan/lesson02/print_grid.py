'''
    Name: Muhammad Khan
    Date: 02/12/2019
    Assignment02

'''

# Part 1.
# Simple print statements to generate a grid.
def print_default_grid():
    print('+'+4*' -'+' +'+4*' -'+' +')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('+'+4*' -'+' +'+4*' -'+' +')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('|'+4*'  '+' |'+4*'  '+' |')
    print('+'+4*' -'+' +'+4*' -'+' +')


# Part 2.***Make it a more general function***
# Generalized function to create the grid.
# The grid size is determined by paramter n.
def print_grid(n):
    n=n//2
    print('+'+n*' -'+' +'+n*' -'+' +')
    for row in range(n):
        print('|'+n*'  '+' |'+n*'  '+' |')
    print('+'+n*' -'+' +'+n*' -'+' +')
    for row in range(n):
        print('|'+n*'  '+' |'+n*'  '+' |')
    print('+'+n*' -'+' +'+n*' -'+' +')


# Part 3.*** Make it an even more general function ***
# The function takes two arguments n1, n2
# The grid is printed based on the number of rows set by n_1, and number of
# columns set by n_2.
def print_grid2(n_1,n_2):
    print(n_1*('+ '+n_2*'- ')+'+')
    counter = 0
    while ( counter < n_1):
        for row in range(n_2):
            print(n_1*('| '+n_2*'  ')+'|')
        print(n_1*('+ '+n_2*'- ')+'+')
        counter+=1

# The main method to test the code.
if __name__ == '__main__':
    print('Part 1')
    print_default_grid()
    print('Part 2')
    print_grid(3)
    print_grid(15)
    print('Part 3')
    print_grid2(3,4)
    print_grid2(5,3)
    print_grid2(6,5)



