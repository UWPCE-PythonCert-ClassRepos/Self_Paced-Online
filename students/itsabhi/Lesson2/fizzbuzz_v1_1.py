def main():

    for i in range(1,101):
        value = ""
        if(i%3 == 0):
            value = "Fizz"
        if(i%5 == 0):    #This appends Buzz to Fizz if the number is divisible by both 3 and 5
            value +="Buzz"
        else:
            value = i
        print(value)





if __name__ == '__main__':
    main()


