def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
    # first check to see if both parameters are met
    # to avoid printing just "fizz" or just "buzz" if 
    #input is divisible by 3 and 5
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
for x in range(1,101):
    # Set the range from 1 to 101 to ensure
    # all 100 lines are printed
    fizzbuzz(x)
