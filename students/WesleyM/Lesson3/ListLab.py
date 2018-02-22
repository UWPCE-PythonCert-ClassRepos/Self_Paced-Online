def fruit1():
    """
    List four fruits, includes a user input to list,
    and removes fruit that start with the letter "P"
    """
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]

    print(fruit)
    
    response = input("Input a fruit > ")

    fruit.append(response)

    print(fruit)
  
    numres = int(input("Input a number > "))
    while numres < 1 or numres > 5:
        print('Input a number between 1 and 5')
        numres = int(input("Input a number > "))
    print(fruit[numres-1])
    response = input("Input another fruit > ")
    fruit = [response] + fruit
    print(fruit)
    response = input("Input another fruit > ")
    fruit.insert(0, response)

    for i in fruit:
        if i[0] == ('P'):
            print(i, end = ' ')
    print()
    return fruit

def fruit2(fruit):
    """
    Displays fruit list, removes the last fruit,
    and deletes a user input fruit
    """
    print(fruit)
    fruit = fruit[:-1]
    print(fruit)
    response = input("Delete a fruit > ")
    while response not in fruit:
        print("Error. Fruit not included. Doubling list.")
        fruit *= 2
        print(fruit)
        response = input("Delete a fruit > ")
    while response in fruit:
        fruit.remove(response)
    print(fruit)

def fruit3(fruit):
    """Asks user if they like fruit and deletes disliked fruit"""
    fruit_like = fruit
    print(fruit_like)
    for i in reversed(fruit_like):
        response = input("Do you like {}? ".format(i))
        while response.lower() != 'yes' and response.lower() != 'no':
            response = input("Please answer 'yes' or 'no':")
        if response.lower() == 'no':
            fruit_like.remove(i)
    print("You like the follow fruit:")
    print(fruit_like)

def fruit4(fruit):
    """
    Makes a copy of the fruit list with the reverse of the letters,
    deletes the last item from original list, and displays both lists
    """
    fruit_copy = []
    for i in fruit:
        fruit_copy += [i[::-1]]
    fruit = fruit[:-1]
    print(fruit_copy)
    print(fruit)

fruits = fruit1()
fruit2(fruits)
fruit3(fruits)
fruit4(fruits)
