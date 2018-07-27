"""Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""


""" draw + - - - - + - - - - +"""
def draw_row_line():
    plus_sign_delimiter=4
    grid_size = 2
    plus_sign = "+"
    minus_sign = "-"
    for x in range((grid_size+1)+(plus_sign_delimiter*grid_size)):
        if(x%5==0):
            print(plus_sign, end='')
        else:
            print(minus_sign, end='')
    print()

"""|         |         |"""
def draw_column_line():
    bar_sign = "|"
    bar_sign_delimiter=4
    grid_size = 2
    for x in range((grid_size+1)+(bar_sign_delimiter*grid_size)):
        if(x%5==0):
            print(bar_sign, end='')
        else:
            print(" ", end='')
    print()

def draw_grid():
    grid_size = 2
    column_height = 4
    for x in range((grid_size+1)+(column_height*grid_size)):
        if(x%5==0):
            draw_row_line()
        else:
            draw_column_line()

if __name__ == '__main__':

    print("test printing lines")
    draw_row_line(0)
    draw_row_line(-1)
    draw_row_line(-2)
    draw_row_line(1)
    draw_row_line(10)

    print("tests printing column")
    draw_column_line(-2)
    draw_column_line(-1)
    draw_column_line(0)
    draw_column_line(1)
    draw_column_line(10)

    print("draw full grid")
    draw_grid()
