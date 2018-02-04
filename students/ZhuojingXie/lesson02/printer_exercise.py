def draw_line1(x=5, y =2):
    i = 0
    while i <y:
        print('+',end = ' ')
        print('- '*x, end = ' ')
        i +=1
    print ('+')
# draw first line, and set default size =5 and unit =2


def draw_line2(x=5, y=2):
    i=0
    while i<y:
        print('|', end = ' ')
        print('  '*x, end =' ')
        i +=1
    print ('|')
# draw second line, and set default size =5 and unit =2


def print_grid(n):
    for y in range (0, 2):
        draw_line1(n)
        for x in range(0, n):
            draw_line2(n)
    draw_line1(n)

def print_grid2(m, n):
    for y in range (0, m):
        draw_line1(n, m)
        for x in range(0, n):
            draw_line2(n,m)
    draw_line1(n,m)
