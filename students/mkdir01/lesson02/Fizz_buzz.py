def print_fizz():
    print("Fizz", end = "")


def print_buzz():
    print("Buzz", end = "")


def FizzBuzz(x=100):
    for num in range(x):  # count from 0 to x-1
        if (num + 1) % 3 == 0:
            print_fizz()
        if (num + 1) % 5 == 0:
            print_buzz()
        if (num + 1) % 3 != 0:
            if (num + 1) % 5 != 0:
                print(num + 1, end="")
        print()  # prints newline

FizzBuzz()
