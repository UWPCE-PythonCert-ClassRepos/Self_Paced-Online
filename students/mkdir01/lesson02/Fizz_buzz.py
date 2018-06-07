def print_fizz():
    print("Fizz", end = "")


def print_buzz():
    print("Buzz", end = "")


def fizz_buzz(x=100):
    for num in range(1, x + 1):  # count from 0 to x-1
        if num % 3 == 0:
            print_fizz()
        if num % 5 == 0:
            print_buzz()
        if (num % 3 != 0) and (num % 5 != 0):
            print(num, end="")
        print()  # prints newline

fizz_buzz()
