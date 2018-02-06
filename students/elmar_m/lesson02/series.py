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
        








if __name__ == '__main__':
    print('i wanna be a module, please import me!')
