#This program prints from 1 to 100
#If number is divisible by 3, prints "Fizz"
#If number is divisible by 5, prints "Buzz"
##If number is divisible by 3 and 5, prints "Fizz Buzz"

for number in range(1,101):
  if number%15==0:
    print ('Fizz Buzz')
  else:
    if number%3==0:
      print("Fizz")
    elif number%5==0:
      print("Buzz")
    else:
      print (number)
