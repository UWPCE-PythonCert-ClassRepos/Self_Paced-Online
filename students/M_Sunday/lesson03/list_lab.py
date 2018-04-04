#!/usr/bin/python

# lesson 03 - list lab exercise


def list_contents(list_, id_=1):
    print("\nSeries List Includes the Following Fruits:")
    for j, item_ in enumerate(list_):
        if id_ == 1:
            print("  - {}".format(item_))


# Series 1
list_1 = ['Apples', 'Pears', 'Oranges', 'Peaches']

list_contents(list_1)

user_val = input("\nAdd Another Fruit to Series List: ")

list_1.append(user_val)

list_contents(list_1)

user_val = input("\nWhich Item in Series 1 List to Display? ")

print("\nItem {} in Series List is {}".format(int(user_val), list_1[int(user_val) - 1]))

user_val = input("\nAdd Another Fruit to Series List: ")

list_1 = [user_val] + list_1

list_contents(list_1)

user_val = input("\nAdd Another Fruit to Series List: ")

list_1.insert(0, user_val)

list_contents(list_1)

print("\nAll the Fruits that Begin with the Letter P Are: ")

for item in list_1:
    if item[0] == 'P':
        print("  - {}".format(item))

# Ends Series 1

# Series 2

list_contents(list_1)

list_1.pop()

list_contents(list_1)

user_val = input("\nWhich Fruit Would you Like to Delete? ")

list_1.remove(user_val)

list_contents(list_1)

# Ends Series 2

# Series 3

list_new = list_1[:]
for item in list_1:
    user_val = input("\nDo you like {}? ".format(item))
    while (user_val != 'No') and (user_val != 'Yes'):
        user_val = input("\nPlease Respond with Either Yes or No")
    if user_val == 'No':
        list_new.remove(item)


list_contents(list_new)

# Ends Series 3

# Series 4

list_copy = list_1[:]

for i, item in enumerate(list_copy):
    list_copy[i] = list_1[i][::-1]

list_1.pop()

list_contents(list_1)

list_contents(list_copy)

# Ends Series 4
