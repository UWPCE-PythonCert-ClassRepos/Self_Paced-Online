def fibonacci(n):
    """Return nth Fibonacci series number"""
    if n<1:return 0
    if n==1:return 1
    return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    """Return nth Lucas series number"""
    if n<1:return 2
    if n==1:return 1
    return lucas(n-1)+lucas(n-2)

def sum_series(n,a=0,b=1):
    """
    Return nth number in series where f(n)=f(n-1)+f(n-2).

    :param n: desired value in series
    :param a=0: optional parameter, determines f(0) in series,
                if a and b are blank, Fibonacci series will be reproduced
    :param b=1: optional parameter, determines f(1) in series,
                if a and b are blank, Fibonacci series will be reproduced

    """
    if n<1:return a
    if n==1:return b
    return sum_series(n-1,a,b)+sum_series(n-2,a,b)

if __name__=='__main__':
    # test fibonacci function by reproducing first 8 values
    test_str=''
    for i in range(8):
        test_str+=str(fibonacci(i))+' '
    assert test_str=='0 1 1 2 3 5 8 13 '
    print('Fibonacci Test: passed')

    # test lucas function by reproducing first 8 values
    test_str=''
    for i in range(8):
        test_str+=str(lucas(i))+' '
    assert test_str=='2 1 3 4 7 11 18 29 '
    print('Lucas Test: passed')

    # test sum_series function by reproducing first 8 values of Fibonacci series
    test_str=''
    for i in range(8):
        test_str+=str(sum_series(i))+' '
    assert test_str=='0 1 1 2 3 5 8 13 '
    print('Sum Series Test 1 - mimic Fibonacci: passed')

    # test sum_series function by reproducing first 8 values of Lucas series
    test_str=''
    for i in range(8):
        test_str+=str(sum_series(i,2,1))+' '
    assert test_str == '2 1 3 4 7 11 18 29 '
    print('Sum Series Test 2 - mimic Lucas: passed')
