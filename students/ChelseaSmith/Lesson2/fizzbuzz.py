for i in range(1, 100):  # creates loop from 1-100
    if i % 3 == 0 and i % 5 == 0:  # handled separately from the elifs so I don't have to deal with newlines
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
