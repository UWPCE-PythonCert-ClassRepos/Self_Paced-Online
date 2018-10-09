fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
def series1(fruits):
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