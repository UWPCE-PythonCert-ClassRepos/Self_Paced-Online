#Joshua Bone - UW Python 210 - Lesson 2
#FizzBuzz Exercise

def fizzBuzz():
  for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0: print(i, end='') 
    if i % 3 == 0: print("Fizz", end='') 
    if i % 5 == 0: print("Buzz", end='') 
    print()
    
#fizzBuzz()
if __name__ == "__main__":
  fizzBuzz()
