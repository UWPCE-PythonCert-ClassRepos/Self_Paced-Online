def print_grid():
    a = ' - '
    a = a * 4
    b = '+'
    c = '|'
    spacing = '  '
    spacing = spacing * 6
    for j in range(2):
        print (b , a , b , a, b )
        for i in range(4):
            print (c , spacing , c , spacing , c)
            print ('')
    print (b , a , b , a , b )


