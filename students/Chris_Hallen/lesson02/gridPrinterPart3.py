def gridPrinter(boxLength, trimLength):
    """This function draws a similar grid with a specified number of rows and columns, and with each cell a given size"""
    row = ' - '
    space = '   '
    plus = '+'
    col = '|'

    fullRow = (plus + (row * trimLength + plus) * boxLength) + '\n'
    partialRow = fullRow.replace(plus, col)
    partialRow = partialRow.replace(row, space)

    print(fullRow + ((partialRow * trimLength) + fullRow) * boxLength)


gridPrinter(3, 4)


gridPrinter(5, 3)
