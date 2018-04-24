# Goal:
# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.


# Fizzbuzz to 100
def fizzbuzz():
    counter = 1
    while counter <= 100:
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz")
            counter += 1
        elif counter % 3 == 0:
            print("Fizz")
            counter += 1
        elif counter % 5 == 0:
            print("Buzz")
            counter += 1
        else:
            print(counter)
            counter += 1


# Fizzbuzz dynamic number
def fizzbuzz_with_entry(number):
    counter = 1
    while counter <= number:
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz")
            counter += 1
        elif counter % 3 == 0:
            print("Fizz")
            counter += 1
        elif counter % 5 == 0:
            print("Buzz")
            counter += 1
        else:
            print(counter)
            counter += 1
