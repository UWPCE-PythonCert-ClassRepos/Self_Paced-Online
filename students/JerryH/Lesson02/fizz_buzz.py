def fizz_buzz():
  for i in range(1,101): #Looing from 1 to 100 inclusive
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)
