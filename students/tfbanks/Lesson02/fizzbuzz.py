#FizzBuzz Exercise by tfbanks

def fizzbuzz(x,y,z): #Defines a function print Fizz, Buzz, and FizzBuzz
                #x is value 1, y is value 2, z is the max value wanted
                
    for n in range(z+1): #n+1 insures the max value (z) is included
        if n%x == 0 and n%y == 0: # first criteria will print FizzBuzz when n is a multiple of both x and y
            print ("FizzBuzz") 
        elif n%x == 0 : # second criteria will print Fizz when n is a multiple of x where first criteria isn't already met
            print ("Fizz")
        elif n%y == 0: # third criteria will print Buzz when n is a multiple of y where first criteria isn't already met
            print ("Buzz")
        else:
            print (n) #prints the value of n when when it is not a multiple of either x or y

fizzbuzz (3,5,100) #Runs the funtion for x = 3 and y = 5 for values between 1 and 100