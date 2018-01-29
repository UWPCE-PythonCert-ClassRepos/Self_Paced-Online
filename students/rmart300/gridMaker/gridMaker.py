"""
Gridmaker by Ross Martin
UW Python210 Lesson 2 Assignment
contains three methods to generate custom sized grids
"""

def makeFirstGrid():
    size = 8
    halfsize = int(size/2)
    print_grid2(2,halfsize)

def print_grid(size):
    """function to print 2x2 square grid: size param determines height and width of grid"""
    size = size - 1 if size % 2 != 0 else size
    halfsize = int(size/2)
    print_grid2(2,halfsize)

def print_grid2(rowcol,size):
    """function to print square grid: number of rows and columns and size of each cell of grid are configurable"""
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
