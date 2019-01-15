# Print 2x2 grid for Part I
horizontal = ("+"+"-"*4)*2
vertical = ("|"+" "*4)*2

print(horizontal,end="+")
print()
print(vertical,end="|")
print()
print(vertical,end="|")
print()
print(vertical,end="|")
print()
print(vertical,end="|")
print()
print(horizontal,end="+")
print()
print(vertical,end="|")
print()
print(vertical,end="|")
print()
print(vertical,end="|")
print()
print(vertical,end="|")
print()
print(horizontal,end="+")
print()

#Print a grid based on parameter Part II
#One parameter to control size of grid
def print_grid(bars):
    print(("+"+"-"*bars)*2,end="+")
    print()
    for x in range(bars):
        print(("|"+" "*bars)*2,end="|")
        print()
    print(("+"+"-"*bars)*2,end="+")
    print()
    for x in range(bars):
        print(("|"+" "*bars)*2,end="|")
        print()
    print(("+"+"-"*bars)*2,end="+")
    print()
    return

print_grid(5)

#Print a grid based on parameter Part III
#Two parameters to control rows,columns,unit size
def print_grid_two(count,bars):
    for y in range(count):
        print(("+"+"-"*bars)*count,end="+")
        print()
        for x in range(bars):
            print(("|"+" "*bars)*count,end="|")
            print()
    print(("+"+"-"*bars)*count,end="+")
    print()
    return;

print_grid_two(5,3)