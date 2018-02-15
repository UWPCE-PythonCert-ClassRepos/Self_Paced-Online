
#Question 1
print('+ ', '- ' * 4, '+ ', '- ' * 4, '+')
print('|','         ', '|', '         ', '|')
print('|','         ', '|', '         ', '|')
print('|','         ', '|', '         ', '|')
print('|','         ', '|', '         ', '|')
print('+ ', '- ' * 4, '+ ', '- ' * 4, '+')
print('|','         ', '|', '         ', '|')
print('|','         ', '|', '         ', '|')
print('|','         ', '|', '         ', '|')
print('|','         ', '|', '         ', '|')
print('+ ', '- ' * 4, '+ ', '- ' * 4, '+')

#Question 2
def draw(x):
    print('+', '-' * x, '+', '-' * x, '+')
    for i in range(x):
        print('|',' ' * x, '|', ' ' * x, '|')
    print('+', '-' * x, '+', '-' * x, '+')
    for i in range(x):
        print('|',' ' * x, '|', ' ' * x, '|')
    print('+', '-' * x, '+', '-' * x, '+')

draw(3)


#Question 3
def draw3(x , y):
    hor =  ('+ ' + ('- ' * y )) * x + '+'
    ver =  ('|' + (' ' * (2 * y + 1))) * x + '|'
    print(hor)
    for i in range(x):
        for j in range (y):
          print (ver)
          if j == (y - 1):
            print(hor)

draw3(3,5)
