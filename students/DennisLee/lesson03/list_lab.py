#!/usr/bin/env python3

def series1():
    """
    Add and print fruits to a fruit list.

    :return:  The final fruit list.
    """
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

    return fruits

def series2(fruits):
    """


    :fruits:  The initial fruit list.
    """
    # Make a copy of the fruit list and delete the last fruit
    newlist = fruits[:]
    print_sequence(newlist)

    print(f'\nRemoving the last fruit ({newlist[-1]})...')
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
    print(f'\nDeleting fruit {newlist[response-1]} (position {response})')
    del newlist[response-1]
    print_sequence(newlist)

    # Get rid of any remaining occurrences (caused by list doublings)
    while newlist.count(target) > 0:
        fruit_del_index = newlist.index(target)
        print(f'\nAnd deleting {target} from position {fruit_del_index+1}')
        del newlist[fruit_del_index]
        print_sequence(newlist)
    
def print_sequence(seq):
    """
    Pretty-print a sequence of items (such as a list of fruits).

    :seq:  The sequence to print.
    """
    print('\n\nTHE LIST:')
    for i, j in enumerate(seq):
        print(i + 1, j)  # Print using base 1 for end-user benefit

if __name__ == "__main__":
    series2(series1())