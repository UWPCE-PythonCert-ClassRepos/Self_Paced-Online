#!/usr/bin/env python3

### Series 1 ###
print("\n-----------Beginning Series 1-----------")

fruit_list = ["Apples","Pears","Oranges","Peaches"]
print(fruit_list)

# Add a user specified fruit to the list
another_fruit = input("Specify another fruit: ")
fruit_list.append(another_fruit)
print(fruit_list)

# Print the fruit at a user specified (1-based) index
prompt = "Specify an integer in the range [{:d},{:d}] for the desired fruit: "
item_number = input(prompt.format(1,len(fruit_list)))
item_number = int(item_number)
print("The fruit at index {:d} is {}".format(
        item_number, fruit_list[item_number - 1]))

# Add Blueberries and Kiwi to the front of the list
fruit_list = ["Blueberries"] + fruit_list
print(fruit_list)
fruit_list.insert(0,"Kiwi")
print(fruit_list)

# Display fruits in the list that start with the character 'p'
p_fruits = []
for fruits in fruit_list:
    
    if fruits[0].lower() == 'p': 
        p_fruits.append(fruits)
        
print("Fruits that start with a 'P': " + ",".join(p_fruits))


### Series 2 ####
print("\n-----------Beginning Series 2-----------")

# Delete the last fruit in the list
print(fruit_list)
del fruit_list[-1]
print(fruit_list)

# Delete a fruit specified by the user from the list 
# (after multiplying the list by 2, every occurance is deleted)
fruit_list *= 2
delete_fruit = input("Specify the name of a fruit to delete: ")
while delete_fruit not in fruit_list:
    delete_fruit = input("Specify the name of a fruit to delete: ")

print("Before delete:\n",fruit_list)

n_delete_fruits = fruit_list.count(delete_fruit)
for _ in range(n_delete_fruits):
    fruit_list.remove(delete_fruit)

print("After delete:\n",fruit_list)


### Series 3 ###
print("\n-----------Beginning Series 3-----------")
for fruit in fruit_list[:]:
    
    like_fruit = input("Do you like {}?: ".format(fruit))
    while not (like_fruit.lower() == 'no' or like_fruit.lower() == 'yes'):
        like_fruit = input("Do you like {}?. Specify 'yes' or 'no' :".format(
                fruit))
    
    if like_fruit.lower() == 'no': 
        fruit_list.remove(fruit)
    
print(fruit_list)


### Series 4 ###
print("\n-----------Beginning Series 4-----------")
fruit_copy = fruit_list[:]
for k in range(len(fruit_copy)):
    string_k = fruit_copy[k]
    fruit_copy[k] = string_k[::-1]
    
del fruit_list[-1]
print('original:',fruit_list)
print('copy:',fruit_copy)

