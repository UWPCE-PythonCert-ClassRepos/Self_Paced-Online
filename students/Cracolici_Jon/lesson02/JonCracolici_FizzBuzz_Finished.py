#Jon Cracolici
#FizzBuzz Problem
#UW Python Cert Lesson 2
#simple answer
def fizzbuzz(a,b,fizz=3,buzz=5):
    """This function builds a "FizzBuzz" solution given the starting point, ending point,
	and allows the users to select new values for the "Fizz" and "Buzz" replacements. 
	I used kwargs for Fizz and Buzz to default to the current problem.""" 
    #Put in a try except block to make sure the user isnt throwing random crap in here
    try:
        a= int(a)
        b=int(b)
        fizz=int(fizz)
        buzz=int(buzz)
    except:
        print("Use numbers!")
    #build a list for the range of numbers of interest
    l=range(a,b+1)
    #For loop over list to do the task
    for x in l:
        if x%(fizz*buzz)==0:
            print("FizzBuzz")
        elif x%fizz==0:
            print("Fizz")
        elif x%buzz==0:
            print("Buzz")
        else:
            print(x)
