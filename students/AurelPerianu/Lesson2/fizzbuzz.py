'''Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.'''
def fizzbuzz(a=3,b=5,x=1,y=101):
    for i in range(x,y):
        if i%a==0 | i%b==0:
            print('FizzBuzz')
        elif i%a==0:
            print ('Fizz')
        elif i%b==0:
            print ('Buzz')
        else:
            print (i)
if __name__=="__main__":
  fizzbuzz()
