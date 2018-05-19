# ------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: list_lab.py
# PURPOSE: To manipulate data in a list
# DATE: 05/17/2018
#
# DESCRIPTION: Sequence to move through item(s) in a list and to perform
#              actions on item(s) to alter the makeup of the list.
#
# ------------------------------------------------------------------------

# Data -------------------------------------------------------------------

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]  # instantiate list

# -------------------------------------------------------------------------

# Display -------------------------------------------------------------------

# SECTION I

print("Section I")
print(fruit_list)                          # print out items in list
print()

sec1_list = fruit_list
add_new = str(input("Enter a new fruit to add to the list: ")).capitalize()  # new item to be added to list
print()

sec1_list.append(add_new)                 # append item to existing list
count = len(sec1_list)                    # adjust len(list) to including new entry

print(sec1_list)                          # display list
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
    print(sec1_list[item_at_index - 1])   # search list for index -1 (to account for list indexing-
    print()                               # -at 0 and this program indexing at 1)

add_new_plus = "Plums"                   # new value to be added to list
sec1_list = [add_new_plus] + sec1_list   # add value to beginning of list using '+'
print(sec1_list)                         # display updated list
print()

add_new_insert = "Strawberries"           # new value to be added to list
sec1_list.insert(0,add_new_insert)        # add value to beginning of list using .insert()
print(sec1_list)                          # display updated list
print()

for element in sec1_list:                 # print only items in list that begin with "P"
    if element[:1] == "P":
        print(element)
print()

# SECTION II

print()
print("Section II")
print()

print(sec1_list)                   # display original list
print()


sec1_list.pop()                    # remove last item from list
print(sec1_list)                   # display list
print()

val_delete = str(input("Enter a fruit you want to remove from the list: (string value) ")).capitalize()  # entry to delete
print()


if val_delete in sec1_list:            # search list for entry to delete
    print("Item removed!")
    sec1_list.remove(val_delete)       # delete entry
else:
    print("Value not found in list.")   # if not found, print message

print()
print(sec1_list)                       # display updated list

# SECTION III
print()
print("Section III")
print()

liked_fruits = []                       # storage container for list vals that are "yes"

for fruit in sec1_list:                # for each item in fruit_list
    while True:                         # keep looping until list ended

        user_resp = input("Do you like " + str(fruit) + "? ").lower()    # solicit user input
        print()

        if user_resp != "yes" and user_resp != "no":                # if user doesn't enter "yes" or "no" error msg
            print("Please only answer with 'yes' or 'no'.")
            print()
            continue                          # stay on current item until valid entry

        elif user_resp == "yes":              # if user enters "yes", append value to new list
            liked_fruits.append(fruit)
            break                             # break to next item

        else:                                 # if answer is "no", break to next item without saving
            break

sec1_list = liked_fruits                      # overwrite existing list with liked_fruits

print(sec1_list)                              # print out to user



# SECTION IV

print()
print("Section IV")
print()

reverse_list = []                       # container to hold copy of reversed strings

for item in sec1_list:                  # for item in original list, do this
    reverse_list.append(item[::-1])     # append reversed strings to container

sec1_list.pop()                         # remove last item from non-reversed list
print(sec1_list)                        # print regular list

print(reverse_list)                     # print reversed list
