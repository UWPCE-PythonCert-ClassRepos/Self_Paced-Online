"Print a table grid."


class TableGrid(object):
    """
    Create a square table grid, specifying the number of rows/columns
    and the cell height/width.

    :rows_and_cols:  The number of rows and columns in the grid.

    :cell_size:  The height and width of a grid cell.
    """

    def __init(self, rows_and_cols: int, cell_size: int):
        self.rows_and_cols = rows_and_cols
        self.cell_size = cell_size

    def print_grid(self) -> bool:
        """
        Print a square table grid using plain text characters.

        :return:  True if the function succeeds; False if the function fails.
        """

        horizontal_rule: str = self.build_line(True)
        interior_line: str = self.build_line(False)

        print((horizontal_rule + (interior_line * cell_size)) * rows_and_cols
             + horizontal_rule)
        return True

    def build_line(self, border: bool = False) -> str:
        """
        Build a single horizontal line within the table grid.

        :border:  Whether to create a horizontal rule. True indicates yes;
                  False (default) specifies an interior line (containing just
                  the vertical rules, with spaces in between those borders for
                  the cell interior).

        :return:  The text string for a table line.
        """

        PLUS, MINUS, PIPE, SPACE, LINEFEED = '+', '-', '|', ' ', '\n'
        vertical_line_char: str = PIPE
        inside_char: str = SPACE

        # horizontal rules contain plus & minus characters, not pipes & spaces
        if border:
            vertical_line_char, inside_char = PLUS, MINUS
        
        return (vertical_line_char + SPACE + (inside_char + SPACE) * cell_size
            ) * rows_and_cols + vertical_line_char + LINEFEED


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

    tg = TableGrid()
    tg.print_grid()