# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# name the strings
row = "+ - - - - "
column = "|" + " " * 9
print(row * 2 + "+")
print(column * 2 + "|")
print(column * 2 + "|")
print(column * 2 + "|")
print(column * 2 + "|")
print(row * 2 + "+")
print(column * 2 + "|")
print(column * 2 + "|")
print(column * 2 + "|")
print(column * 2 + "|")
print(row * 2 + "+")


# Make it a function
# print a 2x2 grid with a specific side length

def print_grid(n):
    x = n / 2
    y = int(x)  # convert to integer
    row_1 = ('+ ' + ('-' + ' ') * y + '+ ' + ('-' + ' ') * y + '+')
    column_1 = ('|' + ' ' * n + '|' + ' ' * n + '|')
    column_2 = ('|' + ' ' * (n + 1) + '|' + ' ' * (n + 1) + '|')

    print(row_1)

    for i in range(y):
        if n % 2 != 0:
            print(column_1)
        else:
            print(column_2)
    print(row_1)

    for i in range(y):
        if n % 2 != 0:
            print(column_1)
        else:
            print(column_2)

    print(row_1)


print_grid(3)
print_grid(15)
print_grid(8)


# print a grid with certain squares of a specific side length
def print_grid2(a, b):
    row_2 = ("+ " + "- " * b) * a + "+"
    column_3 = ("|" + " " * (2 * b + 1)) * a + "|"

    return (row_2 + "\n" + (column_3 + "\n") * b) * a + row_2


print(print_grid2(3, 4))
print(print_grid2(5, 8))
