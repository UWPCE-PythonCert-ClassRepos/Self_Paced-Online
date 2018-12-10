# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

for i in range(1, 101):  # format and print number from 1 to 100

    # print(number) #test

    if i % 3 == 0 and i % 5 == 0:  # if the number is multiples of 3 and 5 , print "FizzBuzz"
        print("FizzBuzz")
    elif i % 3 == 0:  # if the number is multiples of 3 only, print "Fizz"
        print("Fizz")
    elif i % 5 == 0:  # if the number is multiples of 5 only print "Buzz"
        print("Buzz")
    else:  # Display result
        print(i)
