# grid_part_final.py
#
# Displays a grid of small boxes based on user input for square size & dimensions.
# Where the user enters a value for x and y, the grid of boxes is x by y in grid size.
#
# Coded by LouReis
#
# A one by one box looks like the following
#       +-+
#       | |
#       +-+

plus='+'
minus='-'
space=' '
bar='|'

def variable_square_row(size,columns):
#This function prints out a row of variable sized squares.
  var_top=plus+(size*minus)+plus+space
  var_mid=bar+(size*space)+bar+space
  for x in range(0,columns):
    print(var_top, end="")
  print()
  for x in range (0,size):
    for x in range (0,columns):
        print(var_mid,end="")
    print()
  for x in range (0,columns):
    print(var_top, end="")
  print()

def variable_size_grid(size,columns,rows):
#This function is to draw out the grid based on size, columns, & rows.
    for x in range (0,rows):
        variable_square_row(size,columns)

def user_input():
#This function prompts the user for the square size & grid dimensions.
  print ('This program prints out a grid of squares.')
  size=int(input('Enter the number for square size: '))
  columns=int(input('Enter the number of columns: '))
  rows=int(input('Enter the number of rows: '))
  print('Here is a',columns,'by',rows,'grid:')
  variable_size_grid(size,columns,rows)

user_input()
