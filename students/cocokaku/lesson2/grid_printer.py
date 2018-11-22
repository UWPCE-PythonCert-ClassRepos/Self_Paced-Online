def print_grid(n=8):
    n = int(n/2)
    plus = '+'
    minus = '-'
    pipe = '|'
    space = ' '
    print(plus+(space+minus)*n+(space+plus+space)+(minus+space)*n+plus)
    print((pipe+space*n*2+(space+pipe+space)+space*n*2+pipe+'\n')*n,end='')
    print(plus+(space+minus)*n+(space+plus+space)+(minus+space)*n+plus)
    print((pipe+space*n*2+(space+pipe+space)+space*n*2+pipe+'\n')*n,end='')
    print(plus+(space+minus)*n+(space+plus+space)+(minus+space)*n+plus)

def print_grid2(r=3,n=4):
    if r<0:r=0
    if n<0:n=0
    plus = '+'
    minus = '-'
    pipe = '|'
    space = ' '
    print(plus,end='')
    for i in range(r):
        print((space+minus)*n+space+plus,end='')
    print()
    for k in range(r):
        for j in range(n):
            print(pipe,end='')
            for i in range(r):
                print(space*n*2+space+pipe,end='')
            print()
        print(plus,end='')
        for i in range(r):
            print((space+minus)*n+space+plus,end='')
        print()

if __name__=="__main__":
    print('Test print_grid():')
    print_grid()
    print('\nTest print_grid(8):')
    print_grid(8)
    print('\nTest print_grid(3):')
    print_grid(3)
    print('\nTest print_grid(15):')
    print_grid(15)

    print('\n\nTest print_grid2():')
    print_grid2()
    print('\nTest print_grid2(3,4):')
    print_grid2(3,4)
    print('\nTest print_grid2(5,3):')
    print_grid2(5,3)
