# grid_part3.py
# Displays a grid of small boxes based on user input for dimensions
# Where the user enters a value for x and y, the grid of boxes is x by y in grid_size
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
top = plus+minus+plus+space
mid = bar+space+bar+space

def square_row(n):
#This function prints out one row of small squares.
  for x in range(0,n):
    print(top, end="")
  print()
  for x in range (0,n):
    print(mid, end="")
  print()
  for x in range (0,n):
    print(top, end="")
  print()

def square_size():
  var=int(input('Enter number for square size: '))
  var_top=plus+(var*minus)+plus+space
  var_mid=bar+(var*space)+bar+space
  return var_top,var_mid

def variable_square_row(n):
#This function prints out one row of variable sized squares.
  for x in range(0,n):
    print(var_top, end="")
  print()
  for x in range (0,n):
    print(var_mid, end="")
  print()
  for x in range (0,n):
    print(var_top, end="")
  print()

def user_input():
#This function prompts the user for the grid dimensions.
  print ('This program prints out a grid of squares.')
  columns=int(input('Enter the number of columns: '))
  rows=int(input('Enter the number of rows: '))
  print('Here is a',rows,'by',columns,'grid:')
  for x in range (0,rows):
    square_row(columns)

def columns_and_rows(num_columns,num_rows):
#This function requires & passes two parameters and prints grid when called.
  for x in range (0,num_rows):
    square_row(num_columns)

user_input()
#Below is a sample of a function call passing two parameters
a=3
b=2
print('Here is a sample function call passing 2 parameters to a function.')
columns_and_rows(a,b)
