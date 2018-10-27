#!/usr/bin/env python3

# Dictionaries
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc

new_dict = {}
new_dict["name"] = "Chris"
new_dict["city"] = "Seattle"
new_dict["cake"] = "Chocolate"

# Display the dictionary.
print(new_dict)
# Delete the entry for “cake”.
new_dict.pop("cake")

# Display the dictionary.
print(new_dict)
# Add an entry for “fruit” with “Mango” and display the dictionary.
new_dict["fruit"] = "Mango"

# Display the dictionary keys.
print(new_dict)
# Display the dictionary values.
print(new_dict.values())
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("cake" in new_dict)
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("Mango" in new_dict.values())


#Dictionaries 2
# Using the dictionary from item 1: 
# Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
dict_two = new_dict.copy()
d = {}

for k, v in dict_two.items():
    t = 0
    t = t + v.lower().count("t")
    d[k] = t
    
print(d)

# Sets 1
s2 = set()
s3 = set()
s4 = set()

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
for i in range(21):
    if i%2 == 0:
        s2.add(i)


for i in range(21):
    if i%3 == 0:
        s3.add(i)
  

for i in range(21):
    if i%4 == 0:
        s4.add(i)


# Display the sets.
print(s2)
print(s3)
print(s4)
# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))
# and if s4 is a subset of s2 (True).
print(s4.issubset(s2))


# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
set_python = set()
for char in "Python":
    set_python.add(char)

set_python.add("i")
print(set_python)
# Create a frozenset with the letters in ‘marathon’.
my_list = []
for char in "marathon":
    my_list.append(char)

my_frozenset = frozenset(my_list)
print(my_frozenset)
# display the union and intersection of the two sets.
print(set_python | my_frozenset)
print(set_python & my_frozenset)


  
