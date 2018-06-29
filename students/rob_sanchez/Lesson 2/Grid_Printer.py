#Grid Printer exercise
def print_grid(n):
    #variables
    grid_size=2

    if n%2 == 0:
        row2_size=n+1
    else: row2_size=n

    size=n/2

    plus='+ '
    minus='- '
    bar='|'
    z=' '

    row=plus + minus*(size) + plus + minus*(size) + plus
    row2=bar + z*(row2_size) + bar + z*(row2_size) + bar

    for x in xrange(grid_size):
        print(plus + minus*(size) + plus + minus*(size) + plus)
        for y in xrange(size):
            print(bar + z*row2_size + bar + z*row2_size + bar)
    print(row)

def print_grid2(grid,size):
    #variables
    plus='+ '
    minus='- '
    bar='| '
    z='  '

    row=minus*(size) + plus

    row2= z*size + bar

    for x in xrange(grid):
        print(plus+row*grid)
        for y in xrange(size):
            print(bar + row2*grid)
    print(plus+row*grid)
