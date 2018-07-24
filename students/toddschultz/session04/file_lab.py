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

def advanced_copy():
	with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04/lorem.txt', 'r') as f3:
		while True:
			line = f3.readline()
			if not line:
				break
			with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/new_copy2.txt', 'w') as f4:
				f4.write(line)

def binary_copy():
	with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04/jeep.jpg', 'rb') as f5:
		with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/new_copy3.jpg', 'wb') as f6:
			f6.write(f5.read())		

def byte_binary_copy():
	with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04/jeep.jpg', 'rb') as f7:
		with open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/new_copy4.jpg', 'wb') as f8:	
			while True:
				buf = f7.read(1)
				if buf:
					f8.write(buf)
				else:
					break