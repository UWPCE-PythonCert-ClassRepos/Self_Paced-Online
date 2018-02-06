'''
elmar_m / 22e88@mailbox.org
-------------------------------
Lesson02:  Fibonacci Series Exercise
'''

def fib(n):
    if n == 0:
        print('value 0 in Fibonacci series: 0')
    elif n == 1:
        print('value 1 in Fibonacci series: 1')
    else:
        counter = 0
        valuelist= [0, 1]
        c = None

        while counter <= n - 2:
            a = valuelist[0]
            b = valuelist[1]
            c = a + b
            valuelist[0] = b
            valuelist[1] = c
            counter += 1

        print('value', n,  'in Fibonacci series:', c)




if __name__ == '__main__':
    print('i wanna be a module, please import me!')
