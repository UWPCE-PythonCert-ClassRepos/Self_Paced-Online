import os

file_to_copy = input('Filename to copy: ')

working_dir = os.getcwd()

file_to_copy_full = os.path.join(working_dir, file_to_copy)

with open(file_to_copy_full, 'rb') as infile:
    copy = infile.read()

copy_to = input('Full filepath to make a copy: ')

with open(copy_to, 'wb') as outfile:
    outfile.write(copy)
    
print('File Copied!')