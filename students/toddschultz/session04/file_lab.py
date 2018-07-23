import os

def full_path():
	path = "/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04"
	files = os.listdir(path)
	for file in files:
		print(path, file)

def file_copy():
	with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04/lorem.txt', 'r') as f1:
		data = f1.read()
	with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/new_copy.txt', 'w') as f2:
		f2.write(data)

file_copy()