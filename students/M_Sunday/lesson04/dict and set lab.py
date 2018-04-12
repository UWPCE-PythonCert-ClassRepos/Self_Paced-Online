#!/usr/bin/python

# Dictionaries 1

data = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print(data)

data.pop('cake')

print(data)

data['fruit'] = 'Mango'

print(data)

print(data.keys())

print(data.values())

if 'cake' in data:
    print("Cake is a key")
else:
    print("Cake is not a key")

if 'Mango' in data.values():
    print("Mango is a value")
else:
    print("Mango is not a value")

# -------------------------

# Dictionaries 2

data2 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

data_cop = data2.copy()

for i in data_cop.keys():
    # new_value = 0
    val = data_cop[i]
    new_value = val.lower().count('t')
    # for j in range(0, len(val)):
    #     if val[j].lower() == 't':
    #         new_value = new_value + 1
    data_cop[i] = new_value

print(data_cop)

# -------------------------

# Sets 1

s2 = {4, 12, 16, 18}

s3 = {3, 6, 9}

s4 = {4, 12, 16}

print(f"{s2}\n{s3}\n{s4}")

print(s3 < s2)

print(s4 < s2)

# -------------------------

# Sets 2

se = {'P', 'y', 't', 'h', 'o', 'n'}

se.add('i')

print(sorted(se))

sef = frozenset({'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'})

print(se | sef)

# -------------------------
