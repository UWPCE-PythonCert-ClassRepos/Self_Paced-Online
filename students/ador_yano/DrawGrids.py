# DrawGrids.py implements the Lesson 2 assignment from UWPCE Python Programming

intro = '''UWPCE Python Programming: Lesson 2 Assignment
Three functions to print grid three ways
1. print_grid1(): display on screen a simple 2 x 2 grid
2. print_grid2(n): display on screen a scalable 2 x 2 grid based on the size specified by the argument "n"
3. print_grid3(a,b): diplay on screen a grid specified by "a" rows & "a" columns of "b" size
'''
print(intro)

def print_grid1():
    for i in range(2):                      # draw 2 rows of 2 columns
        for i in range(2):                  # draw top line
            print("+", "- " * 4, end="")
        print("+")
        for i in range(4):                  # draw row
            for i in range(2):              # draw columns
                print("|", "  " * 4, end="")
            print("|")
    for i in range(2):                      # draw bottom line
        print("+", "- " * 4, end="")
    print("+")




def print_grid2(n):
    scale = n//2                            # convert n to scale defined by assignment
    for i in range(2):                      # draw 2 rows of 2 columns
        for i in range(2):                  # draw top line
            print("+", "- " * scale, end="")    # size side per scale
        print("+")
        for i in range(scale):                  # draw row per scale
            for i in range(2):              # draw columns
                print("|", "  " * scale, end="")
            print("|")
    for i in range(2):                      # draw bottom line
        print("+", "- " * scale, end="")        # size side per scale
    print("+")




def print_grid3(a,b):
    rows = a
    columns = a
    scale = b                            # convert n to scale defined by assignment
    for i in range(rows):                      # draw rows columns
        for i in range(columns):                  # draw top line
            print("+", "- " * scale, end="")    # size side per scale
        print("+")
        for i in range(scale):                  # draw row per scale
            for i in range(columns):              # draw columns
                print("|", "  " * scale, end="")
            print("|")
    for i in range(columns):                      # draw bottom line
        print("+", "- " * scale, end="")        # size side per scale
    print("+")
