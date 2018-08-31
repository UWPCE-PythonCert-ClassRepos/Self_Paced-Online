# Start Dictionaries 1 from Lesson 4
dict1 = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}

print('This is our dictionary')
print(dict1)
dict1.pop('cake')
print('\n'"This is our dictionary after we removed 'cake'.")
print(dict1)
print('\n'"This is our dictionary after we add fruit with mango.")
dict1['Fruit']='Mango'
print('\n''These are the dictionary keys')
print(dict1.keys())
print('\n''These are the dictionary values')
print(dict1.values())
print('\n'"See if 'Cake' is in the dictionary")
print('Cake' in dict1)
print('\n'"See if 'Mango' is in the dictionary")
print('Mango' in dict1.values())

# Starting Dictionaries 2 from Lesson 4
dict1 = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
dict2={}
for i, values in dict1.items():
    count = 0
    for j in values:
        if j.lower() == 't':
            count += 1
    dict2[i]=count

print('\n''This is the result of Dictionary 2')
print(dict2)


# Starting Sets 1 from Lesson 4
s2 ={0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
s3 = {0, 3, 6, 9, 12, 15, 18}
s4 = {0, 4, 8, 12, 16, 20}

print('These are our sets')
print('\n''This is Set s2')
print(s2)
print('\n''This is Set s3')
print(s3)
print('\n''This is Set s4')
print(s3)

#Check if s3 is a subset of s2
print('\n''Check if s3 is a subset of s2')
print(all(x in s2 for x in s3))
print('\n''Check if s4 is a subset of s2')
print(all(x in s2 for x in s4))

# Starting Sets 2 from Lesson 04

s_python=set('Python')
print('\n''Add the letter \'i\' to python')
s_python.update('i')
print(s_python)

s_frozen= frozenset('marathon')
print('\n''This is the frozen set')
print(s_frozen)

# Display the union of the two sets
print('\n''Display the union of the two sets')
print(s_python.union(s_frozen))

#Display the interseciton of the two sets
print('\n''Display the intersection of the two sets')
print(s_python.intersection(s_frozen))