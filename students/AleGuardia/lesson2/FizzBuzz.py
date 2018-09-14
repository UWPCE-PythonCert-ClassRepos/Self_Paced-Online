# FizzBuzz solution by Alejandro Guardia

for i in range(1,101):
    word = ""
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        print(word)
        continue
    print(i)



