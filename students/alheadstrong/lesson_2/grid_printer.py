'''Author: Alex Filson
Updated: 1.15.19
Grid Printer Exercise for Lesson 2
Py210, Online Self-Paced
'''
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

    print(node+space+((horz+space)*size+node+space)*cells)
    for i in range(cells):
        for i in range(size):
            print(vert+space+((space)*((size*2))+vert+space)*cells)
        print(node+space+((horz+space)*size+node+space)*cells)


