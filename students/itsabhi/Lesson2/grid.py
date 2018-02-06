
def print_row_of_bar(g,c):
    bar = "|"
    space = " "
    grid_size = g
    cell_size = c
    while(c>0):
        print (((bar + space + (space+space)*cell_size))*grid_size + bar) 
        c -= 1


def part_2_draw_grid(x):
# This function applies to part two of the exercise, taking an input number that represents the grid size    
    plus = "+"
    minus = "-"
    space = " "

    half_grid = int(x/2)
    print (plus + space + (minus+space)*half_grid + plus + space +(minus+space)*half_grid + plus)
    print_half_grid(half_grid)
    print_half_grid(half_grid)

def print_half_grid(half):
# This function prints a half grid, which contains of lines with "|" and single 'delimiter' line of "+" & "-"
    half_grid = half
    plus = "+"
    minus = "-"
    bar = "|"
    space = " "
    while (half_grid>0):
        print (bar + space + (space+space)*half + bar + space +(space+space)*half + bar)
        half_grid -=1
    
    print (plus + space + (minus+space)*half + plus + space +(minus+space)*half + plus)

def part_3_1_draw_grid(x,y):
#This function applies to part three of the excercise     
    plus = "+"
    minus = "-"
    space = " "
    grid_size = x
    cell_size = y
    print (((plus + space + (minus+space)*y))*x + plus) 
    while (x>0):
        print_row_of_bar(grid_size,cell_size)
        print (((plus + space + (minus+space)*cell_size))*grid_size + plus) 
        x -= 1
    
def main():

    print('+', '- - - -','+', '- - - -','+')
    print('|','       ','|','       ','|')
    print('|','       ','|','       ','|')
    print('|','       ','|','       ','|')
    print('|','       ','|','       ','|')
    print('+', '- - - -','+', '- - - -','+')
    print('|','       ','|','       ','|')
    print('|','       ','|','       ','|')
    print('|','       ','|','       ','|')
    print('|','       ','|','       ','|')
    print('+', '- - - -','+', '- - - -','+')
    
    part_2_draw_grid(15)

    part_3_1_draw_grid(5,3)

if __name__ == "__main__":
    main()
    
