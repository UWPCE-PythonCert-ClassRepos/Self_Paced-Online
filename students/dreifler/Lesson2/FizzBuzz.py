#FizzBuzz

def fizzBuzz():
    for a in range (1, 100):
        if (a % 3 == 0) and (a % 5 == 0):
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else: print(a)

#Test
if __name__ == '__main__':
    fizzBuzz()
