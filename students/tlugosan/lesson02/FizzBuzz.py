# Print numbers from 1 to 100
# but for multiple of 3 print Fizz
# for multiple of 5 print BUzz
# for multiple of both 3 and 5 print FizzBuzz

def fizz_buzz():

    for i in range(1,101):
        output =""
        if(i%3==0):
            output += "Fizz"

        if(i%5==0):
            output += "Buzz"

        if(output==""):
            output += str(i)

        print(output)

if __name__ == '__main__':
    fizz_buzz()