""" Compute and print a generalization of Fibonacci series when the first 2 numbers are custom."""


def iter_gen_fibonacci(input_number, first_number, second_number):
    """Computes Fibonacci numbers when the numbers are parameterized."""
    fib_list = [first_number, second_number]
    if input_number <= 1:
        return fib_list[:input_number + 1]
    for i in range(2, input_number + 1):
        temp = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(temp)
    return fib_list


def print_iter_gen_fibbonaci(input_number, first_number, second_number):
    """Prints Fibonacci numbers when the numbers are parameterized."""
    result_list = iter_gen_fibonacci(input_number, first_number, second_number)
    print(result_list)


def recursive_gen_fibonacci(input_number, first_number, second_number):
    """Computes Fibonacci numbers when the numbers are parameterized."""
    if input_number == 0:
        return first_number
    if input_number == 1:
        return second_number
    return recursive_gen_fibonacci(input_number - 1, first_number, second_number) + recursive_gen_fibonacci(input_number - 2, first_number, second_number)


def print_recur_gen_fibonacci(input_number, first_number, second_number):
    """ Prints computed recursiveFibonacci numbers output."""
    for i in range(input_number + 1):
        print(recursive_gen_fibonacci(i, first_number, second_number), end=" ")
    print()


if __name__ == '__main__':
    print("Fibonacci numbers test:")
    print_iter_gen_fibbonaci(5, 0, 1)
    print_recur_gen_fibonacci(5, 0, 1)

    print("Print Lucas numbers test:")
    print_iter_gen_fibbonaci(5, 2, 1)
    print_recur_gen_fibonacci(5, 2, 1)



