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
