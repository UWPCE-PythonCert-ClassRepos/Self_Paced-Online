
def gridprint(numrow=2,numcol=2, widthofcol=4, hightofcol=4):
    """Returns a user defined grid.

        Parameters
        ----------
        numrow - Define the number of row(s) (default 2)
        numcol - Define the number of column(s) (default 2)
        widthofcol - Define the character width of a column (default 4)
        hightofcol - Define the character hight of a column (default 4)
    """

    firstcol =  "+" + "-" * widthofcol + "+"
    subcol =  "-" * widthofcol + "+"
    firstcolline =  "|" + " " * widthofcol + "|"
    subcolline = " " * widthofcol + "|"

    if (numrow == 1):
        if (numcol == 1):
            print(firstcol)
        elif (numcol > 1):
            print(firstcol + subcol * (numcol -1))

        for i in range(hightofcol):
            if (numcol == 1):
                print(firstcolline)
            elif (numcol > 1):
                print(firstcolline + subcolline * (numcol -1))

        if (numcol == 1):
            print(firstcol)
        elif (numcol > 1):
            print(firstcol + subcol * (numcol -1))

    else:
        for i in range(numrow):
            if (numcol == 1):
                print(firstcol)
            elif (numcol > 1):
                print(firstcol + subcol * (numcol -1))

            for i in range(hightofcol):
                if (numcol == 1):
                    print(firstcolline)
                elif (numcol > 1):
                    print(firstcolline + subcolline * (numcol -1))

        if (numcol == 1):
            print(firstcol)
        elif (numcol > 1):
            print(firstcol + subcol * (numcol -1))
