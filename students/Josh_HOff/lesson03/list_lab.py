fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
#series 1
print(fruits)
response = input('Please add a fruit: ')
fruits.append(response)
print(fruits)
response = input('Please enter a number:')
print(response + ' {}'.format(fruits[int(response) - 1]))
fruits = ['Pomegranates'] + fruits
print(fruits)
fruits.insert(0,'Blueberries')
print(fruits)
for i in fruits:
    if i[0] == 'P':
        print(i)
fruits3 = fruits[:]
fruits4 = fruits[:]
#series 2    
print(fruits)
del fruits[-1:]
print(fruits)
#    response = input('Please delete a fruit: ')
#bullet 4 in series 2
#    fruits.remove(response)
#    print(fruits)
#bonus for series 2
fruits = (fruits * 2)
x = 1
while x == 1:
    response = input('Please delete a fruit: ')
    for i in fruits:
        if i == response:
            fruits.remove(response)
            x = 2
#series 3
for i in fruits3:
    x = 1
    response = input('Do you like {}? '.format(i))
    if response != 'yes' and response != 'no':
        while x == 1:
            response = input('Please choose "yes" or "no": ')
            if response == 'yes' or response == 'no':
                x = 2
    if response == 'no':
        fruits3.remove(i)
print(fruits3)
#series 4
fruits5 = []
for i in fruits4:
    a = str(i)
    fruits5.append(a[::-1])
print(fruits5)
del fruits4[-1:]
print(fruits4)