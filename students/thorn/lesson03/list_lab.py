"""
Lesson 3 - List Lab
"""

def main():
    fruits = series1()
    
    # Pass the original list created in Series1 --> then make new copy in func.
    series2(fruits)
    series3(fruits)
    series4(fruits)

def series1():
    """ Performs a series of actions based off an exisiting list of fruits. 
    """
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(" ".join(item for item in fruits))  # Test printing these in one line.

    # Prompt user for fruit and append to list.
    fruit_add = input("Please enter a fruit: ")
    fruits.append(fruit_add.title())
    print(" ".join(item for item in fruits))

    # Prompt user for number and display the fruit in it's position.  
    # Note: user input of 1 == index[0]
    # Note: if not int --> default to 1 for easy testing.
    try:
        user_fruit = int(input("Please enter a number: "))
    except ValueError:
        user_fruit = 1
    print( "You have selected number {}.  The fruit at this position is {}"
           .format(user_fruit, fruits[user_fruit-1]))  # -1 to get index pos.
    
    # Add fruit to beginning of the list with '+'.
    fruits = ['Tangerine'] + fruits
    print(" ".join(item for item in fruits))

    # Add fruit to beginning of list with 'insert()'.
    fruits.insert(0, "Pomelo")
    print(" ".join(item for item in fruits))

    # Display all fruits that start with 'P'.
    for item in fruits:
        if item[0].upper() == "P":
            print(item)
    
    return fruits

def series2(fruits):
    """ Displays the list.  Removes the last item from the list.  Redisplays 
    the list.  Prompts the user for a fruit, removes that fruit, and display the
    list.  
    """
    # fruits = list(fruits_copy)
    print(" ".join(item for item in fruits))
    # Using del not pop --> no need to return the item.
    del fruits[-1]
    print(" ".join(item for item in fruits))

    # Multiple the list by 2, delete user's choice fruit.
    fruits = fruits * 2
    fruit_removed = input("Please select a fruit to remove: ")
    while fruit_removed.title() in fruits:
        fruits.remove(fruit_removed.title())
    print(fruits)

def series3(fruits):
    """ Prompts user for their opinion of every fruit in the list (lowercase).
    If the user answers no --> delete fruit.  If user answers something other
    than yes/no --> reprompt. 
    """
    # fruits = list(fruits_copy)

    for item in fruits:
        fruit = item.lower()
        user_choice = input(f"Do you like {fruit}?  Yes/No: ")
        user_choice = user_choice.lower()
        while user_choice != "yes" and user_choice != "no":
            user_choice = input(f"Do you like {fruit}?  Yes/No: ")
            user_choice = user_choice.lower()
        if user_choice == "no":
            fruits.remove(fruit.title())
    print(fruits)

def series4(fruits):
    """ Copies and reverses the spelling of each fruit in the original list.
    Deletes the last item from the original list. """
    fruits_copy = []
    for item in fruits:
        fruits_copy.append(item[::-1])
    
    # Remove last item from original list.
    del fruits[-1]

    print(f"Original List: {fruits}")
    print(f"Copied List: {fruits_copy}")


main()