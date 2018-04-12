def grid_draw():
    n = 1
    while n < 12:
        if (n - 1) % 5 == 0:
            print(2 * ('+ ' + 4 * ('- ')) + '+')
        else:
            print(2 * ('| ' + 8 * ' ') + '|')
        n += 1
 