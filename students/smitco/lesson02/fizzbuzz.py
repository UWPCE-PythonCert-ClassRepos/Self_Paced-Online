#print 1-100 with mult. of 3 fizz, 5 buzz, and 3&5 fizzbuzz
def fizzbuzz(num):
    for n in range(num+1):
        if n % 3 == 0 and n % 5 == 0:
            print ("FizzBuzz")
        elif n % 3 == 0:
            print ("Fizz")
        elif n % 5 == 0:
            print ("Buzz")
        else:
            print (n)

fizzbuzz(100)