#part1
def print_no_args():
    p='+'
    m='-'
    v='|'
    s=' '
    i=4
    #define horizontal lines
    x1=p+s+i*(m+s)+p+s+i*(m+s)+p
    x2=v+(2*i+1)*s+v+(2*i+1)*s+v
    #build the grid
    print(x1)
    for i in range(2):
        for j in range(4):
            print (x2)
        print (x1)

#part2
def print_grid(j):
    p='+'
    m='-'
    v='|'
    s=' '
    #floor division; make sure that will have squares
    i=j//2
    x1=p+s+i*(m+s)+p+s+i*(m+s)+p
    x2=v+(2*i+1)*s+v+(2*i+1)*s+v
    print(x1)
    for m in range(2):
        for k in range(i):
            print (x2)
        print (x1)

#part3
def print_grid2(x,y):
    #convert to integers
    x=int(x)
    y=int(y)
    n=5
    p='+'
    m='-'
    v='|'
    s=' '
    #build the horizontal sequences
    chunk=s+y*(m+s)+p
    chunk1=(2*y+1)*s+v
    ln=p
    ln1=v
    #dynamically build the horizontal lines
    for i in range(x):
        #print (i)
        ln+=chunk
        ln1+=chunk1
    print (ln)
    #dinamically build the squares/grid
    for i in range(x):
        for j in range(y):
            print (ln1)
        print (ln)

if __name__ == "__main__":
    print_no_args()
    print_grid(3)
    print_grid2(3,4)
    print_grid2(5,3)
