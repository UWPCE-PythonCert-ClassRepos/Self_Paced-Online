#Part 1 - No Variables
def print_grid0():
    plus = '+' + ' '
    minus = '-' + ' '
    vertical = '|' + ' '*9
    together = plus + minus*4
    print(together*2 + '+')
    print(vertical*2 + '|')
    print(vertical*2 + '|')
    print(vertical*2 + '|')
    print(vertical*2 + '|')
    print(together*2 + '+')
    print(vertical*2 + '|')
    print(vertical*2 + '|')
    print(vertical*2 + '|')
    print(vertical*2 + '|')
    print(together*2 + '+')

#Part 2 - Function w/ 1 Variable
def print_grid(n):
    m = n // 2
    plus = '+' + ' '
    minus = '-' + ' '
    together = plus + minus*m
    if n%2 == 0:
        vertical = '|' + ' '*(n+1)
    else:
        vertical = '|' + ' '*n
    if n <= 1:
        print('invalid size inputted - input number > 1')
    else:
        print(together*2 + '+')
        for i in range(m):
           print(vertical*2 + '|')
        print(together*2 + '+')
        for i in range(m):
           print(vertical*2 + '|')
        print(together*2 + '+')

##PART 3 - Function w/ 2 Variables
def print_grid2(n,m):
    plus = '+' + ' '
    minus = '-' + ' '
    vertical = '|' + ' '*((m*2)+1)
    together = plus + minus*m
    if m <= 0 or n <= 0:
        print('invalid size inputted - input number > 0')
    else:
        for i in range(n):
            print(together*n + '+')
            for j in range(m):
                print(vertical*n + '|')
        print(together*n + '+')

#####END OF ASSIGNMENT
