def print_grid(x):
    plus = '+'
    minus = '-'
    bar = '|'
    for num in range(x):
	    print((x*(plus + (x*minus)) + plus))
	    for i in range(0,x):
		    print((x*(bar + (x*' ')) + bar))
	    
    print((x*(plus + (x*minus)) + plus))
   
        
def large_grid(x):
    plus = '+'
    minus = '-'
    bar = '|'
    for num in range(x):
	    print((x//2*(plus + (x//2*minus)) + plus))
	    for i in range(0,x//2):
		    print((x//2*(bar + (x//2*' ')) + bar))
	    
    print((x//2*(plus + (x//2*minus)) + plus))   

	
def variable_grid(x,y):
    plus = '+'
    minus = '-'
    bar = '|'
    for num in range(x):
	    print((y*(plus + (y*minus)) + plus))
	    for i in range(0,y):
		    print((y*(bar + (y*' ')) + bar))
	    
    print((y*(plus + (y*minus)) + plus))	
 
