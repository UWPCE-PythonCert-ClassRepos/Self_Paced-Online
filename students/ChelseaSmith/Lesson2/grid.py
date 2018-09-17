plus = ("+ " + "- " * 4) * 2 + "+"  # variable for top/bottom of cells to save me typing
vert = ("|" + " " * 9) * 2 + "|"  # variable for sides of cells to save me typing

print(plus)  # print top of first row of cells
for i in range(4):  # print sides of first row of cells
    print(vert)
print(plus)  # print line between first and second row of cells
for i in range(4):  # print sides of second row of cells
    print(vert)
print(plus)  # print bottom of second row of cells