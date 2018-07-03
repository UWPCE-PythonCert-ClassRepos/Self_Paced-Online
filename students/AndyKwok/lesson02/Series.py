# Description: Program that prints out Fibonacci or Lucas series depending on user input
# Author: Andy Kwok
# Last Updated: 07/01/2018
# ChangeLog: 
#			v1.0 - Initialization


def	Fib_series(n):
    """Function to show Fibonacci series
    n: number to display in the series 
    """
    series = [0, 1]
    for i in range(2, n):
        series += [series[i-2] + series[i-1]]
    print('The' + 'th number of the Fibonacci series is: ', series[n-1])
    print('The entire series is: ' , series)

def Luc_series(n):
    """Function to show Lucas series
    n: number to display in the series 
    """
    series = [2, 1]
    for i in range(2, n):
        series += [series[i-2] + series[i-1]]
    print('The' + 'th number of the series is: ', series[n-1])
    print('The entire series is: ' , series)

def sum_series(n, x=0, y=1):
    """Generalized function to perform both Fibonacci or Lucas series
    n: number of elements in the series to print
    x: 1st value in the series , (No input == display Fibonacci series)
    y: 2nd value in the series , (No input == display Fibonacci series)
    """
    series = [x, y]
    for i in range(2, n):
        series += [series[i-2] + series[i-1]]
    print('The' + 'th number of the series is: ', series[n-1])
    print('The entire series is: ' , series)