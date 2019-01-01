def print_grid0():
    print_grid2(2,4)

def print_grid(number):
    if number%2>0:
        scale=int((number-1)/2)
        print_grid2(2,scale)
    else:
        scale=int(number/2)
        print_grid2(2,scale) 

def print_grid2(pluses,minuses):
    plus='+'
    minus='-'
    m=0
    print(plus+pluses*(minus*minuses+plus))
    while m<pluses:
        lower_grid(pluses,minuses,plus,minus)
        m+=1

def lower_grid(pluses,minuses,plus,minus):
    n=0
    while n<minuses:    
        print("|"+pluses*(" "*minuses+"|"))
        n+=1
    print(plus+pluses*(minus*minuses+plus))
	
	