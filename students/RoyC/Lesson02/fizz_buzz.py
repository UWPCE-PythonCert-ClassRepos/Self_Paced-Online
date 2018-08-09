# iterate from 1 to 100
for i in range(1, 100):
    rem3 = i % 3
    rem5 = i % 5
    if rem3 == 0 or rem5 == 0:
        # printing fizz or buzz or both
        if (rem3 == 0):
            print("fizz", end="")
        if (rem5 == 0):
            print("buzz", end="")
    else:
        # not a multiple of either, print number
        print(i, end="")
    
    # line feed    
    print()    