# Classic FizzBuzz problem, prints value 1 through 100 or Fizz if divisible by 3, Buzz if divisible by 5
# and FizzBuzz if divisible by both, otherwise prints the value

for i in range(1, 101):
    if (i % 15 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)