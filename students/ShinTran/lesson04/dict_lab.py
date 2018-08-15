'''
Shin Tran
Python 210
Lesson 4 Assignment
'''


# Dictionaries 1
info_dict = {'name':'Shin', 'city':'Seattle', 'cake':'Strawberry'}
print(info_dict)
info_dict.pop('cake')
print(info_dict)
info_dict['fruit'] = 'Mango'
print(info_dict)
for keys in info_dict:
	print(keys)
for keys, values in info_dict.items():
	print(values)
print("Is cake a key in info_dict? " + str('cake' in info_dict))
print("Is Mango a value in info_dict? " + str('Mango' in info_dict.values()))
print()


# Dictionaries 2
info_dict2 = info_dict.copy()
print(info_dict2)
for keys in info_dict2:
	t_counter = 0
	for i in range(0,len(keys)):
		if keys[i] == 't':
			t_counter = t_counter + 1
		info_dict2[keys] = t_counter
print(info_dict2)
print()


# Sets 1
s2 = set()
s3 = set()
s4 = set()
for i in range(0,21):
	if (i % 2 == 0):
		s2.add(i)
	if (i % 3 == 0):
		s3.add(i)
	if (i % 4 == 0):
		s4.add(i)
print("s2: " + str(s2))
print("s3: " + str(s3))
print("s4: " + str(s4))
print("Is s3 a subset of s2? " + str(s3 < s2))
print("Is s4 a subset of s2? " + str(s4 < s2))
print()


# Sets 2
py_set = set(list("python"))
print(py_set)
py_set.add('i')
print(py_set)
fz_set = set(list("marathon"))
print(fz_set)
print("Union of the two sets: " + str(sorted(py_set.union(fz_set))))
print("Intersection of the two sets: " + str(sorted(fz_set.intersection(py_set))))
print()


# Prints the full path for all files in the current directory
import pathlib
current_dir = pathlib.Path('.')
for file in current_dir.iterdir():
	print(str(current_dir.absolute()) + "\\" + str(file))
print()


# Copies the contents from a file source, creates a new file with the same contents
# (without using shutil, or the OS copy command)
file = open('Text1.txt')
contents = file.read()
#print(contents)
output = open('Text1_Copy.txt','w')
output.write(contents)
output.close()
file.close()

'''
# Testing to see if the output looks good
file_copy = open('Text1_Copy.txt')
contents = file_copy.read()
print(contents)
file_copy.close()
'''

# Advanced: make it work for any size file:
# i.e. don’t read the entire contents of the file into memory at once
# Tested with a .jpg and a .docx file
with open('Text2.jpg', 'rb') as infile, open('Text2_Copy.jpg', 'wb') as outfile:
	outfile.write(infile.read())
with open('Text3.docx', 'rb') as infile, open('Text3_copy.docx', 'wb') as outfile:
	outfile.write(infile.read())

