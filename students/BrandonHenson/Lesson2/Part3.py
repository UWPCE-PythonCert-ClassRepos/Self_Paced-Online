def print_grid2(n, v):
    plus = '+'
    minus = ' - '
    pipe = '|'
    space = '   '
    top = minus * v + plus
    top1 = plus + top * n
    middle = (pipe + space * v)*n + pipe
    print(top1)
    for i in range(n):
        for i in range(v):
            print(middle)
        print(top1)
print_grid2(4,4)