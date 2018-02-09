for i in range(1,101):
    currentprint = str(i)
    if i % 3 == 0:
        currentprint = currentprint.replace(str(i),"")
        currentprint += "fizz"
    if i % 5 == 0:
        currentprint = currentprint.replace(str(i),"")
        currentprint += "buzz"
    print(currentprint)
    currentprint = ""
