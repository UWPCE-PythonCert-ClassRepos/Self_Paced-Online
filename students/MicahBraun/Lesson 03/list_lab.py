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

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
count = len(fruit_list)
print("Length of list: ", count)
# -------------------------------------------------------------------------


# Processing --------------------------------------------------------------


# ---------------------------------------------------------------------------


# Display -------------------------------------------------------------------

# SECTION I

print(fruit_list)                                                            # print list
print()
add_new = str(input("Enter a new fruit to add to the list: ")).capitalize()  # item to add

fruit_list.append(add_new)                                                  # append item to list
count = len(fruit_list)
print("Length of list: ", count)
print(fruit_list)                                                            # display list
print()

item_at_index = int(input("Enter a number between 1 and " + str(count) + " print "
                          "index value at that index: "))


print("You entered: ", item_at_index)

