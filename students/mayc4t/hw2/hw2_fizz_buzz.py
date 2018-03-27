# ################################################################################
# Goal:

# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.


# ################################################################################
def fb_print():
    for i in range(1,101):
        if i%15 == 0:
            print ("FizzBuzz ")
            continue
        if i%3 == 0 :
            print ("Fizz ")
            continue
        if i%5 == 0 :
            print ("Buzz ")
            continue
        print(i)

if __name__== "__main__":
    print 
    print ("**"*8 + "Fizz Buzz printing problem"+ "**"*8)
    fb_print()
    print ("**"*8 + " THE END "+ "**"*8)

