#Jon Cracolici
#Lesson 2 Gridprint Problem
#UW Python Cert
#
#
def gridprint0():
#This is the super basic function with no arguments. It just builds the grid seen at the beginning of the problem.
    cellnum0 = 2  #number of cells in a row or column. Assumed square.
    lnum = 4     #number of dashes between vertices
    rnum = cellnum0*(lnum+1)+1  #count of total row numbers
    i = range(rnum)
    r1 = cellnum0*("+ "+lnum*"- ")+"+"
    r2 = cellnum0*("| "+lnum*"  ")+"|"
    for x in i:
        if x%(lnum+1)==0:
            print(r1)
        else:
            print(r2)

gridprint0()

def gridprint1(L):
#This function makes a grid with edge length L counted as the length between the terminal points. The grid
#will have 4 internal cells.
#I basically use the observation that there are only 2 types of rows in the grids to try to make it simpler. I decided to cast the
#input as an int, which would result in rounding fractional numbers down.
    try:
        l=int(L)
    except:
        print("use a number!")
    cellnum1 = 2
    rnum = cellnum1*(l//2+1)+1         #local variable that counts number of total rows
    i = range(rnum)
    r1=cellnum1*("+ "+l//2*"- ")+"+"    #1st type of row
    r2=cellnum1*("| "+l//2*"  ")+"|"     #2nd type of row
    for x in i:
        if x%(l//2+1)== 0:
            print(r1)
        else:
            print(r2)

gridprint1(3)
gridprint1(15)

#NOTE: The problem statements shift the definitions of what the input lengths mean between part 2 and 3. Parts 1 and 2 the input length is the total length between
#the terminal vertices. In Part 3 it is the lenght of the dashed section between the vertices in each box.

def gridprint2(N,E):
#This function makes a grid with edge length E counted as dashes, and grid cells N
#I basically use the observation that there are only 2 types of rows in the grids to try to make it simpler. I decided to cast the
#inputs as ints, which would result in rounding fractional numbers down.
    try:
        n=int(N)
        e=int(E)
    except:
        print("use numbers!")
    rnum = n*(e+1)+1           #local variable that counts number of total rows
    i = range(rnum)
    r1=n*("+ "+e*"- ")+"+"    #1st type of row
    r2=n*("| "+e*"  ")+"|"     #2nd type of row
    for x in i:
        if x%(e+1)== 0:
            print(r1)
        else:
            print(r2)
    
gridprint2(3,4)
gridprint2(5,3)
