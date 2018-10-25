## NEIMA SCHAFI, LESSON 2 Assignment - FizzBuzz

def fizzbuzz():
    for i in range(100):
        n = i+1
        if n%5 == 0 and n%3 == 0:
            print('FizzBuzz')
        elif n%5 ==0:
            print('Buzz')
        elif n%3 == 0:
            print('Fizz')
        else:
            print(n)
