#!/usr/bin/env python3


##########  Dictionaries 1  ##########
print('\n\n-------------- Dictionaries 1 --------------')
my_d = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(my_d)

del my_d["cake"]
print(my_d)

my_d["fruit"] = "Mango"
print("Keys: ",my_d.keys())
print("Values: ",my_d.values())
print("Cake is a key: ", "cake" in my_d)
print("Mango is a value: ", "Mango" in my_d.values())

##########  Dictionaries 2  ##########
print('\n\n-------------- Dictionaries 2 --------------')
t_dict = dict(zip(my_d.keys(), 
                  [key.lower().count('t') for key in my_d.values()]))
print(t_dict)


##########  Sets 1  ##########
print('\n\n-------------- Sets 1 --------------')
s2 = set([k for k in range(0,21) if k % 2 == 0])
s3 = set([k for k in range(0,21) if k % 3 == 0])
s4 = set([k for k in range(0,21) if k % 4 == 0])
print("s2: ", s2)
print("s3: ", s3)
print("s4: ", s4)
print("s3 is a subset of s2: ", s3.issubset(s2))
print("s4 is a subset of s2: ", s4.issubset(s2))

##########  Sets 2  ##########
print('\n\n-------------- Sets 2 --------------')
s_py = set("Python")
s_mar = frozenset("marathon")
print("Union of s_py and s_mar: ", s_py.union(s_mar))
print("Intersection of s_py and s_mar: ", s_py.intersection(s_mar))


##########  File Lab  ##########
print('\n\n-------------- File Lab --------------')

for file in os.listdir():
    print(os.path.abspath(file))

