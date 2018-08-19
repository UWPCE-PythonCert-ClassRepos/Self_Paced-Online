#Part 1 - Making the grid
print('+','-'*4,'+','-'*4,'+')
print('|',' '*4,'|',' '*4,'|')
print('|',' '*4,'|',' '*4,'|')
print('|',' '*4,'|',' '*4,'|')
print('|',' '*4,'|',' '*4,'|')
print('+','-'*4,'+','-'*4,'+')
print('|',' '*4,'|',' '*4,'|')
print('|',' '*4,'|',' '*4,'|')
print('|',' '*4,'|',' '*4,'|')
print('|',' '*4,'|',' '*4,'|')
print('+','-'*4,'+','-'*4,'+')

#Part 2 - Make the Grid Scalable
def grid(scale):
    print('+','-'*scale,'+','-'*scale,'+')
    for i in range(scale):
	    print('|',' '*scale,'|',' '*scale,'|')
    print('+','-'*scale,'+','-'*scale,'+')
    for i in scale:
	    print('|',' '*scale,'|',' '*scale,'|')
    print('+','-'*scale,'+','-'*scale,'+')

grid(3)