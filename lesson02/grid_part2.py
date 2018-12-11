# grid_part2.py
# Displays a grid of small boxes based on user input for dimensions
# Where the user enters a value for y, the grid of boxes is y by y in grid_size
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

def grid2(n):
  for x in range(0,n):
    print(top, end="")
  print()
  for x in range (0,n):
    print(mid, end="")
  print()
  for x in range (0,n):
    print(top, end="")
  print()

def grid_size(y):
  for x in range (0,y):
    grid2(y)

def user_input():
  print ('This program prints out a grid of squares.')
  y=int(input('Enter grid size: '))
  grid_size(y)

user_input()
