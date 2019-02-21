'''
    Name: Muhammad Khan
    Date: 02/12/2019
    Assignment02

    '''

# Part 1.

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

def print_grid2(n_1,n_2):
    print(n_1*('+ '+n_2*'- ')+'+')
    counter = 0
    while ( counter < n_1):
        for row in range(n_2):
            print(n_1*('| '+n_2*'  ')+'|')
        print(n_1*('+ '+n_2*'- ')+'+')
        counter+=1


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



