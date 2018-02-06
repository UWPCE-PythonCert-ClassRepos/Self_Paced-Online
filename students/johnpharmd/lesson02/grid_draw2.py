def grid_draw2(h, w):
    n = 1
    while n < h * 5 + 2:
        if (n - 1) % 5 == 0:
            print(w * ('+ ' + 4 * ('- ')) + '+')
        else:
            print(w * ('|' + 9 * ' ') + '|')
        n += 1
 