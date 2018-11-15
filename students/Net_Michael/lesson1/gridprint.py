

def print_grid( x, y):
    
    for j in range( x):        
        plus = '+'
        minus = '-'
        lay1 = ( plus + (minus * x )) * x + plus
        lay2 = ( '\n' + ('|' + ' ' * x ) * x + '|') * y
        print(lay1, end = ' ')
        print(lay2)
    print(lay1)

