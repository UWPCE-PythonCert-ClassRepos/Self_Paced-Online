def print_grid1():
    for n in range(2):
        a1 = '+ ' + '- ' * 4
        print(a1 * 2, '+', sep='')
        a2 = '|' + ' ' * 8 + ' '
        for m in range(4):
            print(a2 * 2, '|', sep='')
    print(a1 * 2, '+', sep='')


def print_grid2(n):
    for j in range(2):
        a1 = '+ ' + '- ' * n
        print(a1 * 2, '+', sep='')
        a2 = '|' + ' ' * n * 2 + ' '
        for m in range(n):
            print(a2 * 2, '|', sep='')
    print(a1 * 2, '+', sep='')


def print_grid3(n, m):
    a1 = '+ ' + '- ' * m
    print(a1 * n, '+', sep='')
    for j in range(n):
        for it in range(m):
            a2 = '|' + ' ' * m * 2 + ' '
            print(a2 * n, '|', sep='')
        print(a1 * n, '+', sep='')
