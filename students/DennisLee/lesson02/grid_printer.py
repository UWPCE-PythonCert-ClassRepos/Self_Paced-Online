"Print a table grid."

def print_grid(rows_and_cols: int, cell_size: int) -> bool:
    """
    Print a square table grid using plain text characters.

    :rows_and_cols:  The number of rows and columns in the grid.
    :cell_size:  The height and length of a grid cell.

    :return:  True if the function succeeds; False if the function fails.
    """

    horizontal_rule: str = build_line(rows_and_cols, cell_size, True)
    interior_line: str = build_line(rows_and_cols, cell_size, False)

    # Print the top horizontal borders for each table row
    for i in range(rows_and_cols):
        print(horizontal_rule)

        # Print the interior lines within each table row
        for j in range(cell_size):
            print(interior_line)

    print(horizontal_rule) # Print the bottom border for the bottom table row
    return True

def build_line(rows_and_cols: int, cell_size: int, border: bool = False) -> str:
    """
    Build a single horizontal line within the table grid.

    :rows_and_cols:  The number of rows and columns in the grid.
    :cell_size:  The height and length of a grid cell.
    :border:  Whether to create a horizontal rule. True indicates yes;
              False specifies an interior line (containing just the vertical
              rules, with spaces in between those borders for the cell 
              interior).

    :return:  The text string for a table line.
    """

    PLUS, MINUS, PIPE, SPACE = '+', '-', '|', ' '
    vertical_line_char: str = PIPE
    inside_char: str = SPACE

    # horizontal rules contain plus and minus characters, not pipes and spaces
    if border:
        vertical_line_char, inside_char = PLUS, MINUS
    
    return (vertical_line_char + SPACE + (inside_char + SPACE) * cell_size
           ) * rows_and_cols + vertical_line_char

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--table_size", type = int, 
                        help = "specify the number of rows or columns in the \
                        table (default 4)")
    parser.add_argument("-c", "--cell_size", type = int,
                        help = "specify the height and width of a table cell \
                        (default 6)")
    args = parser.parse_args()

    if args.table_size:
        rows_and_cols: int = args.table_size
    else:
        rows_and_cols = 4

    if args.cell_size:
        cell_size: int = args.cell_size
    else:
        cell_size = 6

    print_grid(rows_and_cols, cell_size)