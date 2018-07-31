""" Compute Lucas numbers in multiple ways. """


def compute_lucas_numbers(input_number):
    """Computing recursively Lucas numbers."""
    first_number = 2
    second_number = 1
    if input_number == 0:
        return first_number
    if input_number == 1:
        return second_number
    return compute_lucas_numbers(input_number - 1) + compute_lucas_numbers(input_number - 2)


def print_lucas_numbers(input_number):
    """Printing recursive implementation of Lucas numbers."""
    for i in range(input_number + 1):
        print(compute_lucas_numbers(i), end=" ")


def compute_iterative_lucas_numbers(input_number):
    """Iterative implementation of Lucas numbers."""
    lucas_list = [2, 1]
    if input_number <= 1:
        return lucas_list
    for i in range(2, input_number + 1):
        temp = lucas_list[i - 1] + lucas_list[i - 2]
        lucas_list.append(temp)
    return lucas_list


def print_iterative_lucas_numbers(input_number):
    """Printing iterative implementation of Lucas numbers"""
    result_list = compute_iterative_lucas_numbers(input_number)
    print(result_list)


if __name__ == '__main__':
    print_lucas_numbers(3)
    print()
    print_iterative_lucas_numbers(3)
