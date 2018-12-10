"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    December 9th 2018
"""

#Dictionaries 1:
print("\nThe starting dictionary:")
starting_dict = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(starting_dict)
del starting_dict["cake"]
print("\nDictionary after removing \'cake\':")
print(starting_dict)
starting_dict["fruit"] = "Mango"
print("\nDictionary after adding \'fruit\':")
print(starting_dict)
print("\nListing all the keys:")
print(starting_dict.keys())
print("\nListing all the values:")
print(starting_dict.values())
print("\nIs \'cake\' currently a key?:")
print("cake" in starting_dict.keys())
print("\nIs \'Mango\' currently a value?:")
print("Mango" in starting_dict.values())
print()

#Dictionaries 2:
#Starting the dictionary over.
starting_dict = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(starting_dict)
second_dict = {} #Will be used to copy keys but change values to 't' count.
for item in starting_dict:
    count = 0 #Count for the amount of 't' in values.
    for i in starting_dict[item]:
        if i.lower() == 't': #For each character - lower case and check if 't'
            count += 1
    second_dict[item] = count #After the loop add the count as a value.
print(second_dict) #Print out. Chris = 0, Seattle = 2, Chocolate = 1 - success

#Sets 1:
s2 = set()
s3 = set()
s4 = set()
for i in range(1, 21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2:
py_set = set('Python')
print(py_set)
py_set.add('i')
print(py_set)
fr_marathon = frozenset('marathon')
print(fr_marathon)
print(py_set | fr_marathon) #Union of the two sets.
print(py_set & fr_marathon) #Intersection of the two sets


#File lab:
import pathlib
pth = pathlib.Path('./')
pth.is_dir()
pth.absolute()
for p in pth.iterdir():
    print(p)
"""
header_size = 4096
test_in = open('test_in.txt', 'w')
with open('test_out.txt', 'r') as f:
    test_in.write(f.read())
test_in.close()
"""
