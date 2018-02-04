def draw_line1(x=3, y =2):
    i = 0
    while i <y:
        print('+',end = ' ')
        print('- '*x, end = ' ')
        i +=1
    print ('+')
# draw first line, and set default size =3 and unit =2


def draw_line2(x=3, y=2):
    i=0
    while i<y:
        print('|', end = ' ')
        print('  '*x, end =' ')
        i +=1
    print ('|')
# draw second line, and set default size =3 and unit =2


def print_grid(n=3):
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



print_grid()  #print 2*2 unit with size 3 by using print_grid() at default setting

print_grid(3)
print_grid(8) #check out the print_grid() functiong

print_grid2(3,4)
print_grid2(6,3) #check out the prin_grid() function
