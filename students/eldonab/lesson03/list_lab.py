#!/usr/bin/env python3



# # Series 1

# # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
# OR:
fruit_ap = []
def fruit_list():
    fruit_ap.append("Apples")
    fruit_ap.append("Pears")
    fruit_ap.append("Oranges")
    fruit_ap.append("Peaches")
    return fruit_ap
fruit_list()
# # # Display the list (plain old print() is fine…).
print(fruit)
print(fruit_ap)
# # # Ask the user for another fruit and add it to the end of the list.
response=input("please, name another fruit. ")
fruit.append(response.capitalize())
# # # # Display the list.
print(fruit)
# # # Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
num = int(input("please, type a number. "))
print(f"{num}: {fruit[num]}")
# # # Add another fruit to the beginning of the list using “+” and display the list.
another_fruit = ["Mango"]
fruit = another_fruit + fruit
print(fruit)
# # # Add another fruit to the beginning of the list using insert() and display the list.
fruit.insert(0, "Avocado")
print(fruit)
# # # Display all the fruits that begin with “P”, using a for loop.
for i in fruit:
    if i[0] == "P":
        print(i)


# # # Series 2
# # # Using the list created in series 1 above:

# # # Display the list.
print(fruit)
# # # # Remove the last fruit from the list.
fruit.pop()
# # # # Display the list.
print(fruit)
# # # Ask the user for a fruit to delete, find it and delete it.
to_delete = input("Please, name a fruit to delete: ")
def remove_fruit(L):
    if to_delete.capitalize() in L:
        for i in L:
            if i == to_delete.capitalize():
                L.remove(i)
    else:
        print("Your choice is not in our list")

    

remove_fruit(fruit)
print(fruit)
# # # # (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

fruit2 = fruit * 2
print(fruit2)
to_delete_all = input("Please, name a fruit to delete: ")
def remove_fruit_all(L):
    while to_delete_all.capitalize() in L:
        for i in L:
            if i == to_delete_all.capitalize():
                L.remove(i)
    return L

print(remove_fruit_all(fruit2))





# # # Series 3

# # # # Again, using the list from series 1:
fruit_original = ["Apples", "Pears", "Oranges", "Peaches"]
# # # # Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
def fruit_pref_simple(fruit_l):
    for item in fruit_l:
        input(f"do you like {item.lower()}? ")
fruit_pref_simple(fruit_original)
# # # # # For each “no”, delete that fruit from the list.

def fruit_preference(fruit_l):
    for item in fruit_l[:]:
        if input(f"do you like {item.lower()}? ")== "no":
            fruit_l.remove(item)
    
    print(fruit_l)
    return fruit_l

fruit_preference(fruit_original)

# # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
def fruit_preference_update(fruit_l):
    for fruit in fruit_l[:]:
        user_res = str(input(f"do you like {fruit.lower()}? "))
        while user_res not in ["yes", "no"]:
            user_res = str(input(f"do you like {fruit.lower()}? Please answer 'yes' or 'no': "))
        if user_res == "no":
            fruit_l.remove(fruit)
    print(fruit_l)
    return fruit_l
         

fruit_new = ["Apples", "Pears", "Oranges", "Peaches"]

fruit_preference_update(fruit_new)






    
# # Display the list.
print(fruit_original)




# # Series 4
# # Once more, using the list from series 1:
fruit_four = ["Apples", "Pears", "Oranges", "Peaches"]


# # # Make a copy of the list and reverse the letters in each fruit in the copy.
fruit_copy = fruit_four.copy()
print(fruit_copy)
def reversed_copy():
    new_fruit = []
    for fruit in fruit_copy:
        new_fruit.append(fruit[::-1])
    return new_fruit


print(reversed_copy())
        
    


# # Delete the last item of the original list. Display the original list and the copy.

fruit_four.pop()

print(fruit_four)
print(fruit_copy)
