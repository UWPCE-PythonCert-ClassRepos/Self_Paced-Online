# function accepts a single parameter to adjust size


def print_grid(x):
    # defines symbol components of the horizontal and vertical lines
    pipe = "|"
    horiz = " - "
    corner = "+"
    # prints the horizontal lines and corners
    print(corner + horiz * x + corner + horiz * x + corner)
    # sets the pipe counter then prints the pipes
    pipe_count = x
    while pipe_count > 0:
        print(pipe + " " * 3 * x + pipe + " " * 3 * x + pipe)
        pipe_count = pipe_count-1
    print(corner + horiz * x + corner + horiz * x + corner)
    pipe_count = x
    while pipe_count > 0:
        print(pipe + " " * 3 * x + pipe + " " * 3 * x + pipe)
        pipe_count = pipe_count-1
    print(corner + horiz * x + corner + horiz * x + corner)
