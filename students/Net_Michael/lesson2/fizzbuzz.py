

def fizzbuzz(a):
    b = list(range(a+1))[:1]
    
    for b in range(a+1)[-a:]:
        if (b % 3 == 0 | b % 5 == 0):
            print("FizzBuszz")
        elif b % 3 == 0:
            print("Fizz")
        elif b % 5 == 0:
            print( "Buzz")
        else:
            print(b)

