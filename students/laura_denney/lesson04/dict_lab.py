

# Dictionaries 1
chris = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(chris)
chris.pop("cake")
print(chris)
chris["fruit"] = "Mango"
print(chris)
print(chris.keys())
print(chris.values())
print("cake" in  chris)
print("Mango" in chris.values())

# Dictionaries 2
chris2 = {}
for keys in chris:
    chris2[keys] = chris[keys].lower().count("t")
print(chris2)

#Sets 1
s2 = set()
s3 = set()
s4 = set()
for num in range (0,20):
    if num % 2 == 0:
        s2.update([num])
        if num % 4 == 0:
            s4.update([num])
    elif num % 3 == 0:
        s3.update([num])
print(s2, s3, s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2
pyset = set('Python')
pyset.add('i')
froset = frozenset('marathon')
print("Union", pyset.union(froset))
print("Intersection", pyset.intersection(froset))
