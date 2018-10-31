"""
Author: Alyssa Hong
Date: 10/09/2018
Lesson2 Assignments > Grid Printer Exercise
"""

# Goal : Write a function that draws a grid


def print_grid(n):

    print('+', end=' ')
    for i in range(n//2):
         print('-', end=' ')
    print('+', end=' ')
    for i in range(n//2):
        print('-', end=' ')
    print('+')

    for i in range(n//2):
        print('|', end=' ')
        for i in range(n//2):
            print(' ', end=' ')
        print('|', end=' ')
        for i in range(n//2):
            print(' ', end=' ')
        print('|')

    print('+', end=' ')
    for i in range(n//2):
        print('-', end=' ')
    print('+', end=' ')
    for i in range(n//2):
       print('-', end=' ')
    print('+')

    for i in range(n//2):
        print('|', end=' ')
        for i in range(n//2):
            print(' ', end=' ')
        print('|', end=' ')
        for i in range(n//2):
            print(' ', end=' ')
        print('|')

    print('+', end=' ')
    for i in range(n//2):
         print('-', end=' ')
    print('+', end=' ')
    for i in range(n//2):
        print('-', end=' ')
    print('+')


    
def print_grid(n,m):
    for i in range(n):
        for i in range(n):
            print('+', end=' ')
            for i in range(m):
                print('-', end=' ')
        print('+')
        for i in range(m):
            for i in range(n):
                print('|', end=' ')
                for i in range(m):
                    print(' ', end=' ')
            print('|')
    for i in range(n):
        print('+', end=' ')
        for i in range(m):
            print('-', end=' ')
    print('+')



# Part 1: print_grid(8)

print_grid(8)



# Part 2: Making it more general. 
# print_grid(3) and print_grid(15)

print_grid(3)
print_grid(15)



#Part 3: Even more general…
#print_grid2(3,4) and print_grid2(5,3) 


print_grid(3,4)
print_grid(5,3)
