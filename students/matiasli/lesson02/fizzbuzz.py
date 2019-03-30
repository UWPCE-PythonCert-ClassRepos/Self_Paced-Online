# fizzbuzz
# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

# to run, in the terminal, load ipython, import fizzbuzz, then call fizzbuzz.fizzBuzz()

def fizzBuzz():

    for i1 in range(100):
        if ( (i1+1)%15 == 0):
            print("FizzBuzz")
        elif ( (i1+1)%3 == 0):
            print("Fizz")
        elif ( (i1+1)%5 == 0):
            print("Buzz")
        else:
            print(i1+1)
