def print_fizz_buzz() -> None:
    """
    Print numbers 1 to 100, but 'Fizz' or 'Buzz' for multiples of 3 or 5

    :return:  None.
    """
    for j in range(100):
        i = j + 1
        if i % 15 == 0:
            i = 'FizzBuzz'
        elif i % 3 == 0:
            i = 'Fizz'
        elif i % 5 == 0:
            i = 'Buzz'
        print(i)
    return None

if __name__ == "__main__":
    print_fizz_buzz()