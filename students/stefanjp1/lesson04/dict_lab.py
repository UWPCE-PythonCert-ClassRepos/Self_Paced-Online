# Dictionaries 1
new_dict = {'name': 'Chris',
            'city': 'Seattle',
            'cake': 'Chocolate'}

print(new_dict)

new_dict.pop('cake') 

print(new_dict)

new_dict['fruit'] = 'Mango'

print(new_dict)
print(new_dict.keys())
print(new_dict.values())
print('cake' in new_dict)
print('Mango' in new_dict.values())


# Dictionaries 2
for k, v in new_dict.items():
    v = v.lower()
    num_t = v.count('t')
    new_dict[k] = num_t
    
print(new_dict)


# Sets 1
nums = list(range(0,21))
print(nums)

def div_set(nums, divider):
    make_set = list()
    
    for num in nums:
        if num % divider == 0:
            make_set.append(num)
    return set(make_set)
            

s2 = div_set(nums, 2)
print('s2:', s2)
s3 = div_set(nums, 3)
print('s3:', s3)
s4 = div_set(nums, 4)
print('s4:', s4)

print(s3.issubset(s2))
print(s4.issubset(s2))


# Sets 2
s = set(['P','y','t','h','o','n'])
print(s)
s.update('i')
print(s)

m = frozenset(['m','a','r','a','t','h','o','n'])
print(m)

print(s.union(m))
print(s.intersection(m))


