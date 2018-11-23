
#Dictionaries 1

#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
#Display the dictionary.
#Delete the entry for “cake”.
#Display the dictionary.
#Add an entry for “fruit” with “Mango” and display the dictionary.
#Display the dictionary keys.
#Display the dictionary values.
#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
#Display whether or not “Mango” is a value in the dictionary (i.e. True).

print("Dictionaries\n")

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print("\n1. Create and display dictionary\n")
print(d.items())

print("\n2. Delete the entry for 'cake' and display dictionary\n")
d.pop('cake')
print(d.items())

print("\n3. Add an entry for \"fruit\" with \"Mango\" and display the dictionary.\n")
d['fruit'] = 'Mango'
print(d.items())

print("\n4. Display the dictionary keys\n")
print(d.keys())

print("\n5. Display the dictionary values\n")
print(d.values())

print("\n6. Display whether or not \"cake\" is a key in the dictionary\n")
print("cake" in d)

print("\n7. Display whether or not \"Mango\" is a value in the dictionary\n")
print("Mango" in d.values())


#Dictionaries 2

#Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).

print("\nDictionaries 2\n")

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

d = {'name': 'Chris'.lower().count('t'), 'city': 'Seattle'.lower().count('t'), 'cake': 'Chocolate'.lower().count('t')}

print(d.items())


print("\nSets 1\n")

print("\nCreate sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4\nDisplay the sets\n")

num_list = list(range(0,21))

def make_set(num_list, div):
    set_int = set()
    for num in num_list:
        if num % div == 0:
            set_int.add(num)
    return(set_int)


print("s2:", make_set(num_list, 2), "\n")
print("s3:", make_set(num_list, 3), "\n")
print("s4:", make_set(num_list, 4), "\n")

print("Display if s3 is a subset of s2 (False) and if s4 is a subset of s2 (True)\n")

s2 = make_set(num_list, 2)
s3 = make_set(num_list, 3)
s4 = make_set(num_list, 4)

print("s3 in s2: ", s3.issubset(s2) , "\n")
print("s4 in s2: ", s4.issubset(s2)  , "\n")

print("\nSets 2\n")


print("Create a set with the letters in \'Python\' and add \'i\' to the set.\n")

p = {'p','y','t','h','o','n'}
print(p)

p.add('i')
print(p)

print("\nCreate a frozenset with the letters in \'marathon\'.\n")

m = frozenset(('m','a','r','a','t','h','o','n'))
print(m)

print("\ndisplay the union and intersection of the two sets.\n")

print(p.intersection(m))