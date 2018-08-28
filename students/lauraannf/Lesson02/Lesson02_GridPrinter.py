def print_grid1():
    for n in range(2):
        a1 = '+ ' + '- ' * 4
        print(a1 * 2, '+', sep='')
        a2 = '|' + ' ' * 8 + ' '
        for m in range(4):
            print(a2 * 2, '|', sep='')
    print(a1 * 2, '+', sep='')