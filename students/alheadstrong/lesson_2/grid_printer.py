'''Author: Alex Filson
Updated: 1.18.19
Grid Printer Exercise for Lesson 2
Py210, Online Self-Paced
'''

#brute force grid
print('+ '+'- '*4+'+ '+'- '*4+'+')
print('| '+' '*8+'| '+' '*8+'|')
print('| '+' '*8+'| '+' '*8+'|')
print('| '+' '*8+'| '+' '*8+'|')
print('| '+' '*8+'| '+' '*8+'|')
print('+ '+'- '*4+'+ '+'- '*4+'+')
print('| '+' '*8+'| '+' '*8+'|')
print('| '+' '*8+'| '+' '*8+'|')
print('| '+' '*8+'| '+' '*8+'|')
print('| '+' '*8+'| '+' '*8+'|')
print('+ '+'- '*4+'+ '+'- '*4+'+')

def print_grid(n):
    '''single parameter grid. Parameter determines cell size by number of
    dash - space pairs between nodes horizontally and "|" rows vertically.
    '''
    print('+ '+'- '*n+'+ '+'- '*n+'+')
    i = 0
    while i is not n:
        print('| '+' '*2*n+'| '+' '*2*n+'|')
        i+=1
    print('+ '+'- '*n+'+ '+'- '*n+'+')
    i = 0
    while i is not n:
        print('| '+' '*2*n+'| '+' '*2*n+'|')
        i+=1
    print('+ '+'- '*n+'+ '+'- '*n+'+')

def print_grid2(cells,
                size,
                node = '+',
                horz = '-',
                vert = '|',
                space = ' '):
    '''Started with two paramaters, updated to take strings as optional
        parameters. Kwargs must be strings'''
    print(node+space+((horz+space)*size+node+space)*cells)
    for i in range(cells):
        for i in range(size):
            print(vert+space+((space)*((size*2))+vert+space)*cells)
        print(node+space+((horz+space)*size+node+space)*cells)
    #TODO - add exception handling if non-strings are entered in opt params
    # or add a string method to convert




