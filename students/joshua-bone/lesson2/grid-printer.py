#Joshua Bone - UW Python 210 - Lesson 2
#Grid Printer Exercise

#Write a function that draws a grid like the following:
#
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +

# Prints a 2x2 grid having a side length of n
def print_grid(n):
  a=('-'*(n-1)).join('+++')+'\n'
  b=(' '*(2*n-1)).join('|||')+'\n'
  print((b*(n-1)).join([' '.join(a)]*3))

if __name__ == "__main__":
  print_grid(5)
