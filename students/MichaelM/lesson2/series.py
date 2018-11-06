def sum_series(n, n_minus2=0, n_minus1=1):
    """
    Returns a value given a specific term. Either the Fibonacci, Lucas or any other value defined in the term provided.

    {Extended description}

    Parameters:
    n (int): The sequence term
    n_minus2 (int) (opt): The starting point of the sequence
    n_minus1 (int) (opt): The next integer in the sequence

    Returns:
    int: Either the Fibonacci, Lucas or any other value defined in the term provided.

    """

    loop_counter = 1
    # 0, 1 Fib
    # 2, 1 Luc
    # 1, 1 undefined
    term_values = [n_minus2, n_minus1]
    for i in range(1, n - 1):
        new_value = term_values[loop_counter] + term_values[loop_counter - 1]
        term_values.append(new_value)
        loop_counter += 1
    result = max(term_values)
    return result


def assert_correct_input(n, n_minus2, n_minus1):
    """
    Check inputs for whole numbers.

    sum_series requires whole numbers to correctly compute Fibonacci and Lucas series'

    Parameters:
    n: The sequence term
    n_minus2: The starting point of the sequence
    n_minus1: The next integer in the sequence

    Returns:
    string: Results as to whether the inputs all passed or all failed.

    """
    try:
        assert (n % 1) == 0
        assert (n_minus2 % 1) == 0
        assert (n_minus1 % 1) == 0
    except AssertionError:
        result = "int_assertion_failed"
    else:
        result = "ok"
    return result

# 1  2  3  4  5   6   7   8,  9 // term
# 0, 1, 1, 2, 3,  5,  8, 13, 21 // fibonacci
# 2, 1, 3, 4, 7, 11, 18, 29, 47 // lucas
# 1, 1, 2, 3, 5,  8, 13, 21, 34 // undefined
