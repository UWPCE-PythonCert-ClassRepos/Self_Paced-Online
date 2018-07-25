###Lesson 2 Grid Printer Exercise###

###Values###
c = "+"
h = "-"
v = "|"
s = " "
n = 4

###Part 1###
print (c + (h*n) + c + (h*n) + c )
for i in range(n):
   print(v + (s*n) + v + (s*n) + v)
print (c + (h*n) + c + (h*n) + c )
for i in range(n):
   print(v + (s*n) + v + (s*n) + v)
print (c + (h*n) + c + (h*n) + c )

###Part 2###
def print_grid(GridSize):
  print (c + (h*GridSize) + c + (h*GridSize) + c )
  for i in range(GridSize):
     print(v + (s*GridSize) + v + (s*GridSize) + v)
  print (c + (h*GridSize) + c + (h*GridSize) + c )
  for i in range(GridSize):
     print(v + (s*GridSize) + v + (s*GridSize) + v)
  print (c + (h*GridSize) + c + (h*GridSize) + c )
print_grid (5)
print_grid (6)

###Part 3###
def print_grid2(GridSize, cellNum):
    rowStr = ("+" + (" -" * cellNum) + " ") * GridSize + "+"
    colStr = ("|" + (2 * cellNum * " ") + " ") * GridSize + "|"

    print(rowStr)
    for i in range(GridSize):
        for j in range(cellNum):
            print(colStr)
        print(rowStr)
        
print_grid2(2,3)
