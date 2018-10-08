def grid1():
    """Print 2x2 grid, each cell 4x4 spaces"""
    boarder_str = '+ - - - - + - - - - +'
    blank_str =   '|         |         |'
    print(boarder_str)
    for i in range(2):
        for j in range(4):
            print(blank_str)
        print(boarder_str)


def print_grid(cell_size):
    """Print 2x2 grid, each cell is cell_size x cell_size spaces
    cell_size param: type: int
                     value >= 2"""
    boarder_str = '+' + (' -'*(cell_size//2)) + ' +' + (' -'*(cell_size//2)) + ' +'
    blank_str =   '|' + ('  '*(cell_size//2)) + ' |' + ('  '*(cell_size//2)) + ' |'
    print(boarder_str)
    for i in range(2):
        for j in range(cell_size//2):
            print(blank_str)
        print(boarder_str)

def print_grid2(rc, cell_size):
    """Print rcxrc grid, each cell is cell_size x cell_size spaces
    cell_size param: type: int
                     value >= 2
    rc:              type: int
                     value >= 1"""
    boarder_cell = (' -'*(cell_size)) + ' +'
    blank_cell =   ('  '*(cell_size)) + ' |'
    boarder_row = '+' + boarder_cell*rc
    blank_row =  '|' + blank_cell*rc
    print(boarder_row)
    for i in range(rc):
        for j in range(cell_size):
            print(blank_row)
        print(boarder_row)