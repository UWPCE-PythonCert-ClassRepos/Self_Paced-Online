#uw python 210
#lesson 03
#max anderson

#list lab

def fruits():

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)

    print()
    newfruit = input('name a fruit > ')

    fruits.append(newfruit)
    print(fruits)

    print()
    print('provide a number between 1 and', len(fruits), '>')
    a = input('> ')
    print(fruits[int(a)-1])

    fruits = ['limes'] + fruits
    print()
    print('we added limes to the list!')
    print(fruits)

    fruits.insert(0, 'bananas')
    print()
    print('we added bananas to the list as well!')
    print(fruits)

    print()
    print('only a few fruits begin with \'p\':' )

    for fruit in fruits:
        if fruit[0] == 'P' or fruit[0] == 'p':
            print(fruit, end=' ')
        else:
            "no p fruits found"

def fruits_2():

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)

    fruits.pop()
    print(fruits)
    print()

    preference = input('what fruit don\'t you like? >')

    try:
        fruits.remove(preference)
    except ValueError:
        print('didn\'t find that one!')

    print('got rid of it for you: ', fruits)

def fruits_3():

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

    for fruit in fruits[:]:
        preference = input('Do you like {}? '.format(fruit.lower()))
        while (preference != 'yes' and preference != 'no'):
            preference = input('Please answer either \'yes\' or \'no\' >')
        if preference == 'no':
            fruits.remove(fruit)

    print(fruits)
