def fizz_buzz():
    for i in range(100):
        check3=(i+1) % 3
        check5=(i+1) % 5
        if check3 == 0 and not (check5 == 0):
            #print(check3)
            print("fizz")
        elif check5 == 0 and not (check3 == 0):
            print("buzz")
        elif check5 == 0 and (check3 == 0):
            print("fizzbuzz")
        else:
            print(i+1)
            i=i+1