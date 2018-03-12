def formation(grid_size, grid_multi):
    plus = "+ "
    minus = "- "
    space = "  "
    pipe = "| "
    nl_feed = "\n"

    plus_section = plus + minus * grid_size
    pipe_section = pipe + space * grid_size

    plus_row = plus_section * grid_multi + plus + nl_feed
    pipe_rows = pipe_section * grid_multi + pipe + nl_feed

    grid_final = plus_row + (pipe_rows * grid_size + plus_row) * grid_multi

    print(grid_final)

formation(0, 0)
formation(1, 1)
formation(2, 2)
formation(3, 3)
