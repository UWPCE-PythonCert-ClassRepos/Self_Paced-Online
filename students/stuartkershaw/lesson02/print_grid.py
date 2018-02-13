pipe = '|'
plus = '+'
minus = '-'
space = ' '


def set_row(corner, section, size, count):
    row = corner + ' ' + ((section + ' ') * size)
    row = row * count
    row += corner
    return row


def print_grid(size, count=2):
    for i in range(count):
        print(set_row(plus, minus, size, count))
        for i in range(size):
            print(set_row(pipe, space, size, count))
    print(set_row(plus, minus, size, count))


def print_grid_alt(count, size):
    for i in range(count):
        print(set_row(plus, minus, size, count))
        for i in range(size):
            print(set_row(pipe, space, size, count))
    print(set_row(plus, minus, size, count))


print_grid(15)
print_grid_alt(5, 3)
