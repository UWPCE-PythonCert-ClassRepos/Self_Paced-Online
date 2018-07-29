#uw python 210
#lesson 02
#max anderson

# o controls number of cells w/ a default value of 2
# 2 cells are required for a grid
# n controls cell width

def grid_printer(n, o=2):

    # while not necessary verbalizing graphic elements improves
    # legibility of this code

    joint = "+"
    span = "-"
    pipe = "|"
    void = ' '

    row = ''
    column = ''

    # o controls cell number by controlling joint number
    # must add a joint by default
    o += 1

    #build a row and print it
    for i in range(o):
        row += joint

        if i != o-1:
            for i in range(n):
                if i == 0:
                    row+= span
                else:
                    row += void + span

    print(row)

    #build a column and print it

    for i in range(n):
        column = ''
        for i in range(o):
            column += pipe + void*(n + (n-1))

        print(column)

# column and row production has been consistently demonstrated




