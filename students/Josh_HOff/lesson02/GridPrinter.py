#standard 8x8 grid
def grid():
    plus = '+ '
    dash = '- '
    line = '|'
    spaces_9 = '         '
    print(plus + (dash * 4) + plus + dash * 4 + plus)
    print(line + spaces_9 + line + spaces_9 + line)
    print(line + spaces_9 + line + spaces_9 + line)
    print(line + spaces_9 + line + spaces_9 + line)
    print(line + spaces_9 + line + spaces_9 + line)
    print(plus + (dash * 4) + plus + dash * 4 + plus)
    print(line + spaces_9 + line + spaces_9 + line)
    print(line + spaces_9 + line + spaces_9 + line)
    print(line + spaces_9 + line + spaces_9 + line)
    print(line + spaces_9 + line + spaces_9 + line)
    print(plus + (dash * 4) + plus + dash * 4 + plus)

#custom grid depending on number that is input
def print_grid(n):
    plus = '+ '
    dash = '- '
    line = '|'
    if n % 2 == 0:
        spaces_ = ' ' * (n + 1)
    else:
        spaces_ = ' ' * n
    if n % 2 == 1:
        n -= 1
    mid = n / 2
    mid = int(mid)
    print(plus + (dash * mid) + plus + (dash * mid) + plus)
    for x in range(0, n):
        print(line + spaces + line + spaces + line)
        if mid == x + 1:
            print(plus + (dash * mid) + plus + (dash * mid) + plus)
    print(plus + (dash * mid) + plus + (dash * mid) + plus)

#custom grid depending on number of rows/columns and grid cell size
def print_grid2(r,n):
    plus = '+ '
    dash = '- '
    line = '|'
    spaces_ = ' ' * (n * 2 + 1)
    for x in range(0, r):
        if r > 1:
            print(plus + (dash * n) + plus, end='')
            for x in range(0, (r - 1)):
                if x == (r - 1):
                    print((dash * n) + plus)
                if x < (r - 1):
                    print((dash * n) + plus, end='')
        else:
            print(plus + (dash * n) + plus, end='')
        print()
        for x in range(0, n):
            print((line + spaces_) * (r + 1))
    if r > 1:
        print(plus + (dash * n) + plus, end='')
        for x in range(0, (r - 1)):
            if x == (r - 1):
                print((dash * n) + plus)
            if x < (r - 1):
                print((dash * n) + plus, end='')
    else:
        print(plus + (dash * n) + plus)
    
#def print_grid(size, units):
#    minus = ' - '
#    pipe = '|'
#    plus = '+'
#    space = '   '

#    outer = plus + (units * minus + plus) * size
#    middle = pipe + (space * units + pipe) * size

#    for _ in range(size):
#        print(outer)
#        for _ in range(units):
#            print(middle)
#    print(outer)

    
    
    
    
    
    
    
    