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


