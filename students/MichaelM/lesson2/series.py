def fibonacci(n):
    """ 
    Returns a fibonacci value given a specific term.

    {Extended description} 

    Parameters: 
    n (int): The fibonacci sequence term  

    Returns: 
    int: fibonacci value for the term provided
    """
    loop_counter = 1
    result = 0
    n_minus2 = 0
    n_minus1 = 1
    for i in range(1, n):
        i2 = i+1
        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 //first 16
        # cheat for the first iteration...
        if loop_counter == 1:
            result = 0
        # add the last two results
        result = n_minus2 + n_minus1
        # print("Fibonacci iteration: " + str(loop_counter) + ", result: " + str(result) + ",n-2=" + str(n_minus2) + ", n-1=" + str(n_minus1))
        # swap out new values for next loop
        loop_counter += 1
        n_minus1 = n_minus2
        n_minus2 = result
    return result


def lucas(n):
    """ 
    Returns a lucas value given a specific term.

    {Extended description} 

    Parameters: 
    n (int): The lucas sequence term  

    Returns: 
    int: lucas value for the term provided
    """
    loop_counter = 1
    result = 0
    n_minus2 = 2
    n_minus1 = 0
    for i in range(0, n):
        # 2, 1, 3, 4, 7, 11, 18, 29 //first 8
        # cheat for the first 2 iterations...
        if loop_counter == 1:
            result = 2
        if loop_counter == 2:
            result = 1
        # add the last two results for every other lucas number
        else:
            result = n_minus2 + n_minus1
            # print("Loop iteration: " + str(loop_counter) + ", result: " + str(result) + ",n-2=" + str(n_minus2) + ", n-1=" + str(n_minus1))
        # swap out new values for next loop
        loop_counter += 1
        n_minus1 = n_minus2
        n_minus2 = result
    return result
