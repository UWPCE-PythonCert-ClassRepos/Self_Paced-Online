'''
elmar_m / 22e88@mailbox.org
-------------------------------
Lesson02:  Fizz Buzz Exercise
'''


for i in range(1,101):
    # print(i)
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)


if __name__ == '__main__':
    print('i wanna be a module, please import me!')
