# Activity 1
# Dictionaries 1

d = {"name" : "Chris", "city" : "SeatTle", "cake" : "Chocolate"}
print("Original dictionary:")
print(d)
print("\nDictionary with 'cake' removed:")
del d["cake"]
print(d)
print("\nDictionary with a fruit added:")
d["fruit"] = "Mango"
print(d)
print("\nDictionary keys only:")
print(d.keys())
print("\nDictionary values only:")
print(d.values())
print("\nIs the key 'cake' in the dictionary?")
print("cake" in d)
print("\nIs the value 'Mango' in the dictionary?")
print("Mango" in d.values())

# Dictionaries 2
d2 = {}
for key, val in d.items():
    tcount = val.lower().count("t")
    d2[key] = tcount
print("\nNew Dictionary:")
print(d2)

# Sets 1
s2 = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3 = set([0, 3, 6, 9, 12, 15, 18])
s4 = set([0, 4, 8, 12, 16, 20])
print("\nBy two (s2): {}".format(s2))
print("By three (s3): {}".format(s3))
print("By four (s4): {}".format(s4))

print("\nIs s3 a subset of s2? {}".format(s3.issubset(s2)))
print("\nIs s4 a subset of s2? {}".format(s4.issubset(s2)))

# Sets 2
def create_set(s):
    s20 = set()
    for i in s:
        s20.update(i)
    return s20

print("\nPython in a set:")
s5 = create_set("python")
print(s5)
print("\nPython in a set with 'i':")
s5.update("i")
print(s5)

print("\nFrozen set:")
s6 = create_set("marathon")
s7 = frozenset(s6)
print(s7)

print("\nUnion of pythoni and marathon set:")
s8 = s5.union(s7)
print(s8)

print("\nintersection of pythoni and marathon set:")
s9 = s5.intersection(s7)
print(s9)

y = input() # hold open
