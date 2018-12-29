def print_grid2(pluses,minuses):
    plus='+'
    minus='-'
    m=0
    print(plus+pluses*(minus*minuses+plus))
    while m<pluses:
        lowergrid(pluses,minuses,plus,minus)
        m+=1
def lowergrid(pluses,minuses,plus,minus):
    n=0
    while n<minuses:    
        print("|"+pluses*(" "*minuses+"|"))
        n+=1
    print(plus+pluses*(minus*minuses+plus))
	
	