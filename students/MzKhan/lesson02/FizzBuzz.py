'''
    Name: Muhammad Khan
    Date: 02/12/2019
    Assignment02

'''

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


if __name__ == "__main__":

    FizzBizz()