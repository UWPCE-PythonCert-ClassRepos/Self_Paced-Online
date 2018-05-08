# ----- Dictionaries 1 -----

cake_dict = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}

print(cake_dict)

cake_dict.pop("cake")

print(cake_dict)

cake_dict["fruit"] = "Mango"

print(cake_dict)

print(cake_dict.keys())

print(cake_dict.values())

print("Is 'cake' still in our dictionary?")
print("cake" in cake_dict)

print("Is 'Mango' still in our dictionary?")
print("Mango" in cake_dict.values())

# ----- Dictionaries 2 -----

cake_dict = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}

t_dict = {}

for k, v in cake_dict.items():
    t_dict[k] = (cake_dict[k].lower().count('t'))

print("Printing the number of times 't' occurs in values...")
print(t_dict)

# ----- Sets 1 -----

s2 = set()
s3 = set()
s4 = set()

for n in range(21):
    if n % 2 == 0:
        s2.update([n])


for n in range(21):
    if n % 3 == 0:
        s3.update([n])

for n in range(21):
    if n % 4 == 0:
        s4.update([n])

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# ----- Sets 2 -----

s5 = set()

for l in 'Python':
    s5.update(l)

print(s5)

s6 = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))

print(s6)

print("Displaying union...")
print(s5.union(s6))

print("Displaying intersection...")
print(s5.intersection(s6))
