#prints a 2x2 grid
def grid(): 
    horz = ('+'+'----')*2+'+'
    vert = ('|'+'    ')*2+'|'
    for i in range(1,12):
        if i == 1 or i==6 or i==11:
            print(horz)
        else:
            print(vert)
    return

#prints a grid x*x grid sized 5 units
def print_grid(x): 
    y = 5
    for i in range(1,x+1):
        for j in range(1,y+1):
            if j%y == 1:
                print(('+'+'-'*y)*x + '+')
                print(('|'+' '*y)*x + '|')
            else:
                print(('|'+' '*y)*x + '|')
    print(('+'+'-'*y)*x + '+')
    return

#prints a grid x*x sized y units
def print_grid2(x,y): 
    
    for i in range(1,x+1):
        for j in range(1,y+1):
            if j%y == 1:
                print(('+'+'-'*y)*x + '+')
                print(('|'+' '*y)*x + '|')
            else:
                print(('|'+' '*y)*x + '|')
    print(('+'+'-'*y)*x + '+')
    return
