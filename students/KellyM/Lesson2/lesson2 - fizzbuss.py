def fizzbuzz():
    """ This function checks a range of numbers from 1 to 100.
        For any number that is divisible by both 3 and 5, it substitutes
        the word Fizzbuzz for the number.
        For any number divisible by 5, it substitutes with the word Buzz.
        For any number divisible by 3, ik substitutes with the work Fizz."""
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)
