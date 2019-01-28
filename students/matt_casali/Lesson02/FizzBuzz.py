"""Print the numbers from 1 to 100. I used the lowest common denominator of 3 and 5 (15) to print FizzBuzz.
Otherwise, if the remainder x divided by 5 or 3 equals 0, it would print Buzz or Fizz"""

for x in range(1, 101):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)