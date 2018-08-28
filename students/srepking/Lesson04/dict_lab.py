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
dict2={}
for i, values in dict1:
	for j in values:
		count=0
		if values[j].lower()='t'
		    count+=1
	dict2[i]=count
print('\n''This is the result of Dictionary 2')	