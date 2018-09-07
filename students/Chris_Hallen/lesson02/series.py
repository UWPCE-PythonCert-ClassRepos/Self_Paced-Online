def fibonacci(numIndex):
    """
        This function prints the fibonacci series up to an index that is entered in the function call
        starting at an index of zero.
    """
    fibList = [0, 1]
    for num in range(2, numIndex + 1):
        fibList.append(fibList[-1] + fibList[-2])

    print(fibList[-1])


def lucas(numIndex):
    """
        This function prints the lucas series up to an index that is entered in the function call
        starting at an index of one.
    """
    fibList = [2, 1]
    for num in range(2, numIndex + 1):
        fibList.append(fibList[-1] + fibList[-2])

    print(fibList[-1])


def sum_series(numIndex, num1=0, num2=1):
    """
        This function prints a series of numbers up to an index that is entered in the function call
        starting at an index of one.  There is one requied parameter and two optional parameters.  By
        default, if no optional parameters are entered, this function prints the fibonacci series.
    """
    num_list = [num1, num2]
    for num in range(2, numIndex + 1):
        num_list.append(num_list[-1] + num_list[-2])

    print(num_list[-1])


fibonacci(6)  # This function return the 6th number in the fibonacci series starting with an index of zero

fibonacci(10)  # This function return the 10th number in the fibonacci series starting with an index of zero

lucas(6)  # This function return the 6th number in the lucas series starting with an index of zero

lucas(10)  # This function return the 10th number in the lucas series starting with an index of zero

sum_series(numIndex=6, num1=2, num2=1)  # This function return the 6th number in the lucas series starting with an index of zero

sum_series(numIndex=10, num1=2, num2=1)  # This function return the 10th number in the lucas series starting with an index of zero

sum_series(numIndex=6)  # This function return the 6th number in the fibonacci series starting with an index of zero

sum_series(numIndex=10)  # This function return the 10th number in the fibonacci series starting with an index of zero

sum_series(numIndex=4, num1=4, num2=5)
# This function produces another series of numbers - not the fibonacci or lucas series - starting with the numbers
# 4 and 5 going to index 4 beginning with an index of zero
