#!/usr/bin/env python3

def series1():
    """
    Add and print fruits to a fruit list.

    :return:  The final fruit list.
    """
    # Define and print the initial fruit list.
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print_sequence(fruits)

    # Ask the user to add a new fruit to the end of the list
    response = input('\nType another fruit: ')
    fruits.append(response.strip().capitalize())
    print_sequence(fruits)

    # Print a fruit using the position (base 1) specified by the user
    response = input('\nType a fruit number: ').strip()
    while not response.isnumeric() or int(response) <= 0 or int(
            response) > len(fruits):
        response = input('TRY AGAIN: type a fruit number: ').strip()
    print(int(response), fruits[int(response)-1])

    # Add and print lychees to the front of the list
    print('\nAdding lychees to the beginning of the list...')
    fruits = ['Lychees'] + fruits
    print_sequence(fruits)

    # Add and print cranberries to front of the list
    print('\nAdding cranberries to the beginning of the list...')
    fruits.insert(0, 'Cranberries')
    print_sequence(fruits)

    # Print all fruits in the list that start with 'P'
    print("\nFruits that begin with the letter P:")
    for fruit in fruits:
        if fruit[0] == 'P':
            print(fruit)

    return fruits

def series2(fruits):
    """
    Remove the last fruit from a list of fruits, then allow the user to
    specify another fruit to delete (but expand the list two-fold
    whenever the user makes an incorrect selection).

    :fruits:  The initial fruit list.
    """
    # Make a copy of the fruit list and delete the last fruit
    newlist = fruits[:]
    print_sequence(newlist)

    print(f'\nRemoving the last fruit ({newlist[-1].lower()})...')
    newlist.pop()
    print_sequence(newlist)

    # Delete a fruit using the position (base 1) specified by the user
    response = input('\nType a fruit number to delete: ').strip()
    while not response.isnumeric() or int(response) <= 0 or int(
            response) > len(newlist):
        # If the user responds incorrectly, double the size of the fruit list
        newlist *= 2
        print("NOT VALID! FRUIT LIST DOUBLES IN SIZE!!")
        print_sequence(newlist)
        response = input('TRY AGAIN: type a fruit number to delete: ').strip()

    response = int(response)
    target = newlist[response-1]
    print(f'\nDeleting fruit {target.lower()} (position {response})')
    del newlist[response-1]
    print_sequence(newlist)

    # Get rid of any remaining occurrences (caused by list doublings)
    while target in newlist:
        fruit_index = newlist.index(target)
        print(f'\nAnd deleting {target.lower()} from position {fruit_index+1}')
        del newlist[fruit_index]
        print_sequence(newlist)

def series3(fruits):
    """
    Ask the user whether they like a fruit, and delete it if they do not.

    :fruits:  The initial fruit list.
    """
    # Copy and print the initial fruit list.
    newlist = fruits[:]
    print_sequence(newlist)

    # Ask whether the user likes each fruit.
    i, prompt = 0, "Do you like {} (yes/no)? "
    while i < len(newlist):
        fruit = newlist[i]

        # Enforce a yes/no answer from the user
        response = input(prompt.format(fruit.lower())).strip().lower()
        while response not in ('yes', 'no'):
            response = input(prompt.format(fruit.lower())).strip().lower()

        # Delete fruit if the answer is negative.
        if response == 'no':
            newlist.remove(fruit)
            continue  # Do not increment counter, since the next item
                        # will have the same index number now (as we deleted
                        # what had been there)

        i += 1
    
    print("Thank you for your responses.")
    print_sequence(newlist)

def series4(fruits):
    """
    Read each string within the fruit list backwards, delete the last
    fruit, and print out the initial and final lists.

    :fruits:  The initial fruit list.
    """
    newlist = fruits[:]
    for i in range(len(newlist)):
        newlist[i] = newlist[i][::-1]
    newlist.pop()

    print("\n\nORIGINAL")
    print_sequence(fruits)

    print("\n\nMODIFIED")
    print_sequence(newlist)

def print_sequence(seq):
    """
    Pretty-print a sequence of items (such as a list of fruits), using
    base 1 notation for end-user benefit.

    :seq:  The sequence to print.
    """
    print('\nTHE LIST:')
    for i, j in enumerate(seq):
        #print(i + 1, j)
        print(f"{i+1:>4d}: {j}")


if __name__ == "__main__":
    linefeeds = '\n' * 5

    print(linefeeds, '\tSERIES 1:')
    fruits1 = series1()

    input('\nPress Enter to continue to series 2: ')
    print(linefeeds, '\tSERIES 2:')
    series2(fruits1)

    input('\nPress Enter to continue to series 3: ')
    print(linefeeds, '\tSERIES 3:')
    series3(fruits1)

    input('\nPress Enter to continue to series 4: ')
    print(linefeeds, '\tSERIES 4:')
    series4(fruits1)