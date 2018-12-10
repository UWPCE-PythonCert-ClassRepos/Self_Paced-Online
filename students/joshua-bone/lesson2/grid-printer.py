#Joshua Bone - UW Python 210 - Lesson 2
#Grid Printer Exercise

#Write a function that draws a grid like the following:
#
test_output = (
"+ - - - - + - - - - +\n"
"|         |         |\n"
"|         |         |\n"
"|         |         |\n"
"|         |         |\n"
"+ - - - - + - - - - +\n"
"|         |         |\n"
"|         |         |\n"
"|         |         |\n"
"|         |         |\n"
"+ - - - - + - - - - +\n"
)

# Prints a 2x2 grid having a side length of n
def simple_grid(n):
  return grid(2, n)
#   a=' '.join(('-'*(n-1)).join('+++'))+'\n'
#   b=(' '*(2*n-1)).join('|||')+'\n'
#   return (b*(n-1)).join([a]*3)

# Prints an n x n grid having a side length of s
def grid(n, s):
  a = ' '.join(('-'*(s)).join('+'*(n+1)))+'\n'
  b = (' '*(2*s+1)).join('|'*(n+1))+'\n'
  return (b*(s)).join([a]*(n+1))

if __name__ == "__main__":
  assert simple_grid(4) == test_output
  print("Simple 2D grid passed test.\n")
  n, s = 5, 3
  print("Printing a %dx%d grid having side length %d:" % (n, n, s))
  print(grid(5,3))
  n, s = 2, 8
  print("Printing a %dx%d grid having side length %d:" % (n, n, s))
  print(grid(n, s))
  n, s = 8, 2
  print("Printing a %dx%d grid having side length %d:" % (n, n, s))
  print(grid(n, s))
