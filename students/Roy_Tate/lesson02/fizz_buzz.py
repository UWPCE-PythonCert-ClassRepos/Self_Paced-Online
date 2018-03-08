# author: githubtater

def fizz_buzz():
    '''A classic, simple computer science problem'''
    current_number = 1
    while current_number < 101:
        if (current_number % 3 == 0) and (current_number % 5 == 0):
            print("FizzBuzz")
        elif current_number % 3 == 0:
            print('Fizz')
        elif current_number % 5 == 0:
            print('Buzz')
        else:
            print(str(current_number))
        current_number += 1


if __name__ == "__main__":
    fizz_buzz()














































































# author: githubtater