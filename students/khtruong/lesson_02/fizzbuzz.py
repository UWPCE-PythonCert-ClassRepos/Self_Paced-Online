"""Example module docstrings text"""


def print_fizzbuzz():
    """Return classic Fizz Buzz exercise."""

    for i in range(1, 101):
        if i % 15 == 0:  # least common denominator of 3 & 5
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

    return
