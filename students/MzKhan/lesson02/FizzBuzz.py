'''
    Name: Muhammad Khan
    Date: 02/12/2019
    Assignment02

'''

# The method uses the mod division to print the desired message.
# if number is the multiple of 3, it prints Fizz.
# if number is the multiple of 5, it prints Buzz.
# if number is the multiple of 3 AND 5, it prints FizzBuzz.
def FizzBizz():
    for i in range(1,101):
        msg = i
        if (msg % 3 == 0 and msg % 5 == 0):
            msg = 'FizzBuzz'
        elif msg % 3 == 0:
            msg = 'Fizz'
        elif msg % 5 ==0:
            msg = 'Buzz'
        print(msg)

# The main method to test the code.
if __name__ == "__main__":

    FizzBizz()