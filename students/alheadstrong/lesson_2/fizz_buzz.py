'''Author: Alex Filson
Updated: 1.18.19
Fizz Buzz Exercise for Lesson 2
Py210, Online Self-Paced
'''

for i in range(1,101):
    if i%3 ==0 and i%5 == 0:
        print('FizzBuzz')
    if i%3 ==0:
        print('Fizz')
    if i%5 ==0:
        print('Buzz')
    else:
        print(i)