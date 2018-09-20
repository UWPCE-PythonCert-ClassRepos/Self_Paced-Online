#GridPrinterExercise

#Part 2
def print_grid(x):
    plus_line(x)
    space_line(x)
    plus_line(x)
    space_line(x)
    plus_line(x)

def plus_line(x):
    for a in range(0,2):
        print('+ ' + '- ' * x, end ='')
    print('x')

def space_line(x):
    for a in range(0,x):
        for b in range(0,2):
            print('|' + ' ' * (x*2), end = ' ')
        print('|')

#Part 3
def print_grid2(x, y):
    for a in range(0, y):
        plus_line2(x,y)
        space_line2(x,y)
    plus_line2(x,y)

def plus_line2(x, y):
    for a in range(0,y):
        print('+ ' + '- ' * x, end ='')
    print('+')

def space_line2(x, y):
    for a in range(0,x):
        for b in range(0,y):
            print('|' + ' ' * (x*2), end = ' ')
        print('|')

#Test
if __name__ == '__main__':
    print_grid(3)
    print_grid(8)
    print_grid2(3,4)
    print_grid2(5,3)