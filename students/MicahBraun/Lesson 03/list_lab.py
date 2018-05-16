# ------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: list_lab.py
# PURPOSE: 
# DATE: 05/15/2018
#
# DESCRIPTION:
# 
# 
# 
# 
#
# ------------------------------------------------------------------------
'''

    - Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    - Display the list (plain old print() is fine…).
    - Ask the user for another fruit and add it to the end of the list.
    - Display the list.
    - Ask the user for a number and display the number back to the user and the fruit
      corresponding to that number (on a 1-is-first basis). Remember that Python uses
      zero-based indexing, so you will need to correct.
    - Add another fruit to the beginning of the list using “+” and display the list.
    - Add another fruit to the beginning of the list using insert() and display the list.
    - Display all the fruits that begin with “P”, using a for loop.

'''
# Data -------------------------------------------------------------------

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]  # instantiate list


# -------------------------------------------------------------------------


# Processing --------------------------------------------------------------


# ---------------------------------------------------------------------------


# Display -------------------------------------------------------------------

# SECTION I

print(fruit_list)                          # print out items in list
print()

add_new = str(input("Enter a new fruit to add to the list: ")).capitalize()  # new item to be added to list
print()

fruit_list.append(add_new)                 # append item to existing list
count = len(fruit_list)                    # adjust len(list) to including new entry

print(fruit_list)                          # display list
print()
                                           # solicit user's input for index
item_at_index = int(input("Enter a number between 1 and " + str(count) + " print "
                          "index value at that index: "))

print("You entered: ", item_at_index)      # display user's entry back to user

if item_at_index > count:                  # make sure entry is within bounds
    print(item_at_index," is outside of the index scope (1 - " + str(count) + ")!")
elif item_at_index <= 0:                   # we are indexing at 1 - onward, omit <1
    print("Indexing starts at 1!")
else:
    print("Value at index " + str(item_at_index) + ": ", end="")    # print index input to search
    print(fruit_list[item_at_index - 1])   # search list for index -1 (to account for list indexing-
    print()                                # -at 0 and this program indexing at 1)

add_new_plus = "Plum"                      # new value to be added to list
fruit_list = [add_new_plus] + fruit_list   # add value to beginning of list using '+'
print(fruit_list)                          # display updated list
print()

add_new_insert = "Strawberry"              # new value to be added to list
fruit_list.insert(0,add_new_insert)        # add value to beginning of list using .insert()
print(fruit_list)                          # display updated list
print()

for i in fruit_list:                       # print only items in list that begin with "P"
    if i[:1] == "P":
        print(i)

