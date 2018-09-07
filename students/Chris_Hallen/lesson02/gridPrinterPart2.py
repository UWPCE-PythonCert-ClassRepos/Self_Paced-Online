#  Make it a function


def gridPrinter(num):
    """This function takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument."""
    num = num // 2
    row = ' - '
    space = '   '
    plus = '+'
    col = '|'

    fullRow = plus + (row * num) + plus + (row * num) + plus + '\n'
    partialRow = fullRow.replace(plus, col)
    partialRow = partialRow.replace(row, space)

    print(fullRow + (partialRow * num) + fullRow + (partialRow * num) + fullRow)


gridPrinter(3)  # Smaller Grid Print


gridPrinter(15)  # Larger Grid Print
