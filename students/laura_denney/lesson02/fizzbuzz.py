#-------------------------------------------------#
# Title: Fizz Buzz
# Dev:   LDenney
# Date:  October 3, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/3/18, Created File
#-------------------------------------------------#

def fizzbuzz():
    for x in range(1,101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

if __name__ == "__main__":
    fizzbuzz()