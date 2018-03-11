#!/usr/bin/env python3

import sys


space = ' '
ast = '*'


# Series 1 #

print("\n" + ast * 5 + " Series 1 " + ast * 5 + "\n")
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
user_fruit = input('Type another fruit and add it to the list: ')
fruit_list.append(user_fruit)
print(fruit_list)
user_index = int(input('Enter a number and the fruit will be returned: '))
if 0 <= user_index < len(fruit_list):
    print(fruit_list[user_index -1])
else:
    print("The number is out of range.")
# Add another fruit to the beginning of the list using “+” and display the list.
fruit_list.insert(0, 'FirstFruit')
print('Added item using insert() method: ', fruit_list)

print("\nReturning all fruit that begins with letter 'P'")
for item in fruit_list:
    if item[0] == 'P':
        print(item)
    else:
        pass


# Series 2 #

print("\n" + ast * 5 + " Series 2 " + ast * 5 + "\n")
print('Current state of fruit_list: ', fruit_list)

print('Removing last item:')
print(fruit_list.pop(len(fruit_list) - 1))

## BONUS (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
user_remove = input("Enter a fruit to delete: ")
for item in fruit_list:
    if item.lower() == user_remove.lower():
        fruit_list.remove(item)
        print('Removed: ' + item)
    else:
        pass

print(fruit_list)


# Series 3 #

def series_3():
    print("\n" + ast * 5 + " Series 3 " + ast * 5 + "\n")
    print('Current state of fruit_list: ', fruit_list)

    while True:
        for item in fruit_list:
            try:
                response = input("Do you like " + item + "? ")

            except IndexError as e:
                print('Invalid response. Try again.', e)

            if response[0].lower() == 'n':
                fruit_list.remove(item)
                print('Removed ' + item + ' from list.')
            elif response[0].lower() == 'y':
                print('Keeping ' + item.title())
            else:
                print('Invalid Response.')


        return False

series_3()


# Series_4  ##

def series_4():
    print("\n" + ast * 5 + " Series 4 " + ast * 5 + "\n")
    orig_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print('The original list is: ' + str(orig_list))
    print('Copying original list...')
    copy_list = orig_list[:]
    print('List copied...')
    copy_list = [item[::-1] for item in copy_list]
    print("Copied list, printed in reverse:  " + str(copy_list))
    print("Original list: " + str(orig_list))
    sys.exit()

if __name__ == "__main__":
    series_4()
    sys.exit()