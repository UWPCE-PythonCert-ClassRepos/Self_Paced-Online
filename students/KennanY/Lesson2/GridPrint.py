#This project prints grids.  It has three functions.
#1. Function with no args
#2. Function with one arg; arg is dimension
#3. Function with two args; first arg is num. of rows and column
#==========================================================================
#1. Function with no args.  Default grid size is 9.
#==========================================================================
def printGrid1():
  print('Size:9x9')
  print('+ - - - - + - - - - +')
  print('|         |         |')
  print('|         |         |')
  print('|         |         |')
  print('|         |         |')
  print('+ - - - - + - - - - +')
  print('|         |         |')
  print('|         |         |')
  print('|         |         |')
  print('|         |         |')
  print('+ - - - - + - - - - +')
  print()
printGrid1()

#===========================================================================
#2. Function with one arg.  The parameter represents the size.
#==========================================================================
def printGrid2(size):
  print('Size=',size)
  #Assume max and min for size.  Min length=3, max length=51
  if size<3:
    size=3 #smallest grid size is three
  if size>51:
    size=51

  #Convert size to width
  width=size + 2 #Outer columns

  #If width is even, make it odd
  if width % 2==0:
    width=width+1

  #Where is the middle plus (+)
  plusloc=(width)//2 +1 #This assumes width is always odd here

  #Build full row
  def buildFullRow (w,ploc):
    for column in range(1,w+1):
      if (column==1 or column==ploc or column==w):
        print ('+', end='')
      else:
        print ('-',end='')
    print()

  #Build the body
  for row in range (1,width+1):
    if (row==1 or row==plusloc or row==width):
      buildFullRow(width, plusloc)
    else: #Build the vertical bars
      for column in range (1,width+1):
        if (column==1 or column==plusloc or column==width):
          print ('|', end='')
        else:
          print (' ', end='')
      print () # Next line

printGrid2(10)
#===========================================================================
#3. Function with two args
#First arg is num of rows and columns, second arg is cell size.
#==========================================================================
def buildFlexFullRow(rowcol,size):
  fullrow=''
  #Form full row
  for col in range (1,rowcol+1):
    fullrow=fullrow + '+'
    for psize in range(1,size+1):
      fullrow=fullrow + '-'
  fullrow=fullrow + '+' #Last +
  return fullrow

def printGrid3(rowcol,size):
  print(rowcol, size)
  #Establish limits
  if rowcol<3:
    rowcol=3
  if rowcol>20:
    rowcol=20
  if size<3:
    size=3
  if size>10:
    size=10

  #Convert row and column to character width and height
  widthheight=size*rowcol+ (rowcol+1) # Gives total num of chars on a full row

  #Print the full shape
  for r in range(1,widthheight+1):
    print(buildFlexFullRow(rowcol,size))

printGrid3(6,3)
