'''
elmar_m / 22e88@mailbox.org
-------------------------------
Lesson02:  Fibonacci Series Exercise
'''

'''
def fibonacci(n):

def series(n, v1=1, v2=2):
    value_1 = 0
    value_2  = 1
    value_3 = value_1 + value_2
    print(value_3)
    value_1 = value_2
    value_2 = value_3

# def calc(a, b, c=(a + b)):
#     # c = a + b
#     return(c)

def test():
    print('hello world')
'''

counter = 0
mylist = [0, 1]

while counter < 10:
    a = mylist[0]
    b = mylist[1]
    c = a + b
    print(c)
    mylist[0] = b
    mylist[1] = c
    counter += 1





if __name__ == '__main__':
    print('i wanna be a module, please import me!')
