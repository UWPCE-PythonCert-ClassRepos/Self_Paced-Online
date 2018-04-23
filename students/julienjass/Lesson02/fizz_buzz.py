for i in range(1, 101):
    #Case if number is multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #Case if number is multiple of 3
    elif i % 3 == 0:
        print("Fizz")
    #Case if number is multiple of 5
    elif i % 5 == 0:
        print("Buzz")
    #Case if number is neither multiple of 3 nor 5
    else:
        print(i)
input("Press enter to exit")