# Print fizz for multiples of 3 and Buzz for multiples of 5
for x in range (101):
    if x == 0:
        print(0)
    elif x%3 == 0 and x%5 == 0:
        print("FizzBuz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x)

