#Declaring some simple symbols for the grid
p = '+'
m = '-'
pp = '|'
s = ' '

def grid():
    """This function prints a 2 x 2 grid"""

    #Prints top, middle, bottom
    tmb = p +  (s+m) * 4 + s + p + (s+m) * 4 + s + p
    #Prints a row of pipes
    pipe = '\n' + pp + s * 9 + pp + s * 9 +pp + '\n'

    print((tmb + '\n' + pipe*4 + '\n') * 2 + tmb)

def print_grid(n):
    """This function prints a grid based on the size "n" given"""

    #Determines the grid size based on the 'n' value given
    size = int((n-1)/2)
    #Assign top, middle, bottom rows to tmb
    tmb = p +  (s+m) * size + s + p + (s+m) * size + s + p
    #Assign a row of pipes to 'pipe'
    pipe = '\n' + pp + s * n + pp + s * n +pp + '\n'

    print((tmb + '\n' + pipe*size + '\n') * 2 + tmb)

def print_grid2(size, unit):
    """This function prints a grid based on the size of rows and columns and unit"""

    pm = (p + (s+m) * unit + s)*size + p        #Plus & Minus row
    pipe = (pp + s * (2*unit + 1))*size + pp    #Pipe row
    a_grid_row = pm + '\n' + ('\n'+ pipe + '\n')*unit   #One row of grids
    whole_grid = ('\n' + a_grid_row) * size + '\n' + pm #Get whole grids

    print(whole_grid)
