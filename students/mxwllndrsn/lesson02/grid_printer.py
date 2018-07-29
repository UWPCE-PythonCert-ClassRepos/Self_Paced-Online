#uw python 210
#lesson 02
#max anderson

# o controls number of cells w/ a default value of 2
# 2 cells are required for a grid
# n controls cell width and height

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

    #build our row
    for i in range(o):
        row += joint

        if i != o-1:
            for i in range(n):
                if i == 0:
                    row+= span
                else:
                    row += void + span

    #build our column
    for i in range(n):
        column = ''
        for i in range(o):
            column += pipe + void*(n + (n-1))

    #print the grid
    for i in range(o):
        print(row)
        if i != o-1:
            for i in range(n):
                print(column)




