'''
elmar_m / 22e88@mailbox.org
-------------------------------
Lesson02:  Fibonacci Series Exercise
'''

def fib(n):
    if n == 0:
        print('value 0 in Fibonacci series: 0')
        return 0
    elif n == 1:
        print('value 1 in Fibonacci series: 1')
        return 1
    elif n > 1:
        startvalues = [0, 1]
        counter = 0
        while counter <= n - 2:
            a = startvalues[0]
            b = startvalues[1]
            c = a + b
            print(c)
            startvalues[0] = b
            startvalues[1] = c
            counter += 1
        return c
    else:
        print('This function requires a positive integer')



def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        startvalues = [2, 1]
        counter = 0
        while counter <= n - 2:
            a = startvalues[0]
            b = startvalues[1]
            c = a + b
            # print(c)
            startvalues[0] = b
            startvalues[1] = c
            counter += 1
        return c
    else:
        print('This function requires a positive integer')
        



def sum_series(n, x=0, y=1):
    
    if x == 0 and y == 1:
        print('Fibonacci series requested...')
        if n == 0:
            print('value 0 in Fibonacci series: 0')
            return 0
        elif n == 1:
            print('value 1 in Fibonacci series: 1')
            return 1
        else:
            # calculate(n, 0, 1)
            calculate(n, x, y)
    elif x == 2 and y == 1:
        print('Lucas series requested...') 
        if n == 0:
            print('value 0 in Lucas series: 2')
            return 2
        elif n == 1:
            print('value 1 in Lucas series: 1')
            return 1 
        else:
            # calculate(n, 2, 1)
            calculate(n, x, y)
    else:
        calculate(n, x, y)


def calculate(n, x, y):
        startvalues = [x, y]
        counter = 0
        while counter <= n - 2:
            a = startvalues[0]
            b = startvalues[1]
            c = a + b
            print(c)
            startvalues[0] = b
            startvalues[1] = c
            counter += 1
        return c



if __name__ == '__main__':
    print('i wanna be a module, please import me!')
