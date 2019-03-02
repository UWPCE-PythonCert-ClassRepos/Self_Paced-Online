#!/usr/bin/env python3

#Dictionaries 1
my_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print(my_dict)
my_dict.pop("cake")
print(my_dict)
my_dict["fruit"] = "Mango"
print(my_dict.keys())
print(my_dict.values())
print("cake" in my_dict)
print("Mango" in my_dict.values())

#Dictionaries 2
new_dict = {}
for k, v in my_dict.items():
    new_dict[k] = v.lower().count("t")
print(new_dict)

#Sets 1
s2 = set([num for num in range(1,20) if num%2 == 0])
s3 = set([num for num in range(1,20) if num%3 == 0])
s4 = set([num for num in range(1,20) if num%4 == 0])

print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2
py_set = {'P','y','t','h','o','n'}
py_set.add('i')

m = frozenset(('m','a','r','a','t','h','o','n'))

print(m.union(py_set))
print(m.intersection(py_set))





