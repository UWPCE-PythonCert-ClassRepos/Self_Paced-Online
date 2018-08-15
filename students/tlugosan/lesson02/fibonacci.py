"""Print Fibonacci numbers starting with 0 and 1"""


def fibonacci_numbers(input_number):
    """ computes recursively Fibonacci numbers """
    if input_number <= 1:
        return input_number
    return fibonacci_numbers(input_number - 1) + fibonacci_numbers(input_number - 2)


def print_fibonacci_numbers(input_number):
    """ Prints computed recursive Fibonacci numbers output."""
    for i in range(input_number + 1):
        print(fibonacci_numbers(i), end=" ")


def iterative_fibonacci(input_number):
    """ Computes iteratively Fibonacci numbers."""
    fib_list = [0, 1]
    if input_number <= 1:
        return fib_list
    for i in range(2, input_number + 1):
        temp = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(temp)
    return fib_list


def print_iterative_fibonacci(input_number):
    """ Prints computed iterative Fibonacci numbers."""
    result_list = iterative_fibonacci(input_number)
    print(result_list)


if __name__ == '__main__':

    #    print("This is a recursive implementation")
    #    print_fibonacci_numbers(1)

    print()
    print("This is an iterative implementation")
    print_iterative_fibonacci(5)
