import os

def full_path():
	path = "/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session04"
	files = os.listdir(path)
	for file in files:
		print(path, file)

full_path()