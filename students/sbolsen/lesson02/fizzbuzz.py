#for i in range(1, 101):
#    if i % 3 == 0:
#        print('fizz')
#        if i % 5 == 0:
#            print('buzz')
#            if i % 3 == 0 and i % 5 == 0:
#                print('fizzbuzz')
#    else:
#        print(i)

for i in range(1, 101):
    if i % 3 ==0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
