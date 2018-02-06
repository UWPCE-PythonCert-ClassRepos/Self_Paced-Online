'''
elmar_m / 22e88@mailbox.org
-------------------------------
Lesson02:  Fizz Buzz Exercise
'''


for i in range(1, 101):
    # print(i)
    # if i % 3 == 0:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

if __name__ == '__main__':
    print('i wanna be a module, please import me!')
