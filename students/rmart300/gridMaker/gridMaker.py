import sys

def makeFirstGrid():
    size = 8
    halfsize = int(size/2)
    print_grid2(2,halfsize)

#def print_grid(size):
#    size = size - 1 if size % 2 != 0 else size
#    halfsize = int(size/2)
#    borderRows = [0,halfsize+1,size+2]
    
#    for i in range(0,size+3):
#        borderChar = '+' if i in borderRows else '|'
#        print(borderChar + '-'*halfsize + '+' + '-'*halfsize + borderChar)

def print_grid(size):
    size = size - 1 if size % 2 != 0 else size
    halfsize = int(size/2)
    print_grid2(2,halfsize)

def print_grid2(rowcol,size):

    #print('print_grid2('+str(rowcol)+','+str(size)+')')
    lineToPrint = ('+'+'-'*size)*rowcol+'+\n'
    for i in range(0,rowcol):
        for j in range(0,size):
            lineToPrint += (('|'+' '*size))*rowcol + '|\n'
        lineToPrint += ('+'+'-'*size)*rowcol+'+\n'                
        
    print(lineToPrint)


if __name__ == '__main__':
    print('make first grid') 
    makeFirstGrid()
    print('\nprint_grid(3)')
    print_grid(3)
    print('\nprint_grid(15)')
    print_grid(15)
    print('\nprint_grid2(3,4)')
    print_grid2(3,4)
