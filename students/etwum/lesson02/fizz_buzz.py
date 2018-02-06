
#assigns the initial value of 1 to x
x = 1

#loops while x is less than 101
while(x < 101):
    
    
    #checks if the remainder of dividing x by 3 and 5 is equal to zero
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        
    #moves to this statement if the first statement doesnt pass
    #checks if dividing x by only 3 has a remainder of zero
    elif x % 3 == 0:
        print("Fizz")
    
    #moves to this statement if the second statement doesnt pass
    #checks if dividing x by only 5 has a remainder of zero
    elif x % 5 == 0:
        print("Buzz")
        
    #moves to this statement if the third statement doesnt pass
    #just prints the value of x
    else:
        print(x)
    
    #adds one to the current value of x
    x+=1
    
    