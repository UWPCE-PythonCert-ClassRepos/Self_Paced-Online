for i in range(1,101):
    fizz, buzz = False, False
    if (i % 3) == 0:
        fizz = True
    if (i % 5) == 0:
        buzz = True
    
    if fizz or buzz:
        if fizz:
            print("Fizz", end = '')
        if buzz:
            print("Buzz", end = '')
        print()
    else:
        print(i)
        