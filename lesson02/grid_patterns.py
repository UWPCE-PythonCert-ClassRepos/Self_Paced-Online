"""Author is Antonio V. Alvillar
   Self-Paced-Online Python 210 UWPCE
   November 06 2018 """

#print("name is: ", __name__) < - testing
#Static Grid ( 4 boxes with dash/line between + for joints)
print('+' + '-' * 4 + '+' + '-' * 4 + '+')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('+' + '-' * 4 + '+' + '-' * 4 + '+')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
print('+' + '-' * 4 + '+' + '-' * 4 + '+')

#Grid Function (Size: dashes equal to half of the input parameter)
def print_grid(dashes):
    size = dashes / 2 #size stored as float from division
    newSize = int(size) #convert to int for iteration
    print('+' + '-' * newSize + '+' + '-' * newSize + '+')
    for num in range(newSize):
        print('|' + ' ' * newSize + '|' + ' ' * newSize + '|')
    print('+' + '-' * newSize + '+' + '-' * newSize + '+')
    for num in range(newSize):
        print('|' + ' ' * newSize + '|' + ' ' * newSize + '|')
    print('+' + '-' * newSize + '+' + '-' * newSize + '+')

"""if __name__ == "__main__":
    print("in the main block") < - testing"""

#Grid Function with 2 parameters (column/row, dashes)
def print_grid2(boxes, dashes):
    size = int(dashes) #convert to int for iteration
    # Initialize variables to keep track of loops and breaks
    dashCount = 0
    spaceCount = 0
    colrow = 0
    lineBreak = 0
    while dashCount < boxes: # fencepost loop for first box lines (top)
        print('+' + '-' * size, end='')
        dashCount += 1
    print('+')
    dashCount = 0 # reset dashcount for internal loop
    while colrow < boxes: # loop for the amount of boxes needed
        while lineBreak < size: # break for horizontal dash/space
            while spaceCount < boxes: # loop for horizontal dashes
                print('|' + ' ' * size, end='')
                spaceCount += 1
            print('|') # fencepost
            lineBreak += 1
            spaceCount = 0
        while dashCount < boxes: # loop for the box outlines
            print('+' + '-' * size, end='')
            dashCount += 1
        print('+') # fencepost
        #reinitialize variables and increment column/row (boxes)
        colrow += 1
        lineBreak = 0
        dashCount = 0
        spaceCount = 0