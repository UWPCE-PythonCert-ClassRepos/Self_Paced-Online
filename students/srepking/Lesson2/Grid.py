#Part 1 - Making the grid with No Arguments
print('+','- '*4,'+','- '*4,'+')
print('|','  '*4,'|','  '*4,'|')
print('|','  '*4,'|','  '*4,'|')
print('|','  '*4,'|','  '*4,'|')
print('|','  '*4,'|','  '*4,'|')
print('+','- '*4,'+','- '*4,'+')
print('|','   '*4,'|',' '*4,'|')
print('|','  '*4,'|','  '*4,'|')
print('|','  '*4,'|','  '*4,'|')
print('|','  '*4,'|','  '*4,'|')
print('+','- '*4,'+','- '*4,'+')

#Part 2 - Make the Grid Scalable
def grid(scale):
    print('+','- '*scale,'+','- '*scale,'+')
    for i in range(scale):
	    print('|','  '*scale,'|','  '*scale,'|')
    print('+','- '*scale,'+','- '*scale,'+')
    for i in range(scale):
	    print('|','  '*scale,'|','  '*scale,'|')
    print('+','- '*scale,'+','- '*scale,'+')



#Part 3 - A Function with Two Parameters

def grid_2(rowscolumns,scale):
    if rowscolumns>0:
        for k in range(rowscolumns):
            for i in range(rowscolumns):
	            print('+','- '*scale, end=' ')
            print ('+')
            for j in range(scale):
                for i in range(rowscolumns):
                    print('|','  '*scale, end=' ')
                print ('|')
        for i in range(rowscolumns):
	        print('+','- '*scale, end=' ')
        print ('+')
    else:
        print('Must Enter column/row value greater than zero')
grid_2(5,5)